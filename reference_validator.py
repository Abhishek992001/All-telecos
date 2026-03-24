import os
import json
import base64
import io
import re
from pathlib import Path
from PIL import Image
import fitz
import openpyxl
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

# =========================
# CONFIG
# =========================
load_dotenv()

REFERENCE_DIR = Path("reference_images")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

llm = ChatAnthropic(
    model="claude-haiku-4-5-20251001",
    api_key=ANTHROPIC_API_KEY,
    max_tokens=2048
)

# =========================
# HELPERS
# =========================
def normalize(text):
    return re.sub(r'[^a-z0-9]', '', str(text).lower())

def image_to_base64(image):
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode()

def load_reference_image(filename):
    path = REFERENCE_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"Image not found: {path}")
    return Image.open(path).convert("RGB")

def pdf_to_images(pdf_path):
    images = []
    with fitz.open(pdf_path) as doc:
        for page in doc:
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            images.append(img)
    return images

# =========================
# 🔥 EXCEL PARSER (FIXED)
# =========================
def load_rules_from_excel(excel_path):
    wb = openpyxl.load_workbook(excel_path)
    ws = wb.active

    # Normalize all available images
    available_images = {
        normalize(p.name): p.name for p in REFERENCE_DIR.glob("*.png")
    }

    rules = {}
    counter = 1

    for row in ws.iter_rows(min_row=2, values_only=True):
        rule_text = row[2]      # C
        guidance  = row[7]      # H
        image_file = row[5]     # F
        image_desc = row[4]     # E

        # Must have rule
        if not rule_text or str(rule_text).strip() == "":
            continue

        # Must have guidance
        if not guidance or str(guidance).strip().lower() in ["", "none", "nan"]:
            continue

        matched_image = None

        # 🔥 HANDLE MULTI-LINE IMAGE CELLS
        if image_file:
            file_list = str(image_file).split("\n")

            for f in file_list:
                key = normalize(f.strip())

                for norm_name, actual in available_images.items():
                    if key in norm_name or norm_name in key:
                        matched_image = actual
                        break

                if matched_image:
                    break

        # 🔥 FALLBACK USING DESCRIPTION
        if not matched_image and image_desc:
            key = normalize(image_desc)

            for norm_name, actual in available_images.items():
                if key in norm_name or norm_name in key:
                    matched_image = actual
                    break

        # If still no image → skip safely
        if not matched_image:
            print(f"❌ SKIPPED (no image match): {rule_text}")
            continue

        rules[f"R{str(counter).zfill(3)}"] = {
            "rule": str(rule_text).strip(),
            "guidance": str(guidance).strip(),
            "image": matched_image
        }

        counter += 1

    print(f"✅ Loaded {len(rules)} valid rules")
    return rules

# =========================
# TEXT RULE
# =========================
def check_text_rules(pdf_path):
    with fitz.open(pdf_path) as doc:
        text = "\n".join([p.get_text() for p in doc])

    return [{
        "rule_id": "TEXT001",
        "rule_text": "All text uppercase",
        "verdict": "PASS" if text == text.upper() else "FAIL",
        "evidence": "Basic uppercase check"
    }]

# =========================
# 🔥 CLAUDE VALIDATION
# =========================
def check_batch(batch, pages):
    image_file = batch["image"]
    rules = batch["rules"]

    ref_img = load_reference_image(image_file)
    ref_b64 = image_to_base64(ref_img)

    page_images = [
        {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/png;base64,{image_to_base64(p)}"
            }
        }
        for p in pages
    ]

    rules_text = "\n\n".join([
        f"{rule_id}:\nRule: {rule['rule']}\nGuidance: {rule['guidance']}"
        for rule_id, rule in rules
    ])

    message = [
        {
            "type": "text",
            "text": f"""
You are a telecom QA engineer.

Evaluate ALL rules:

{rules_text}

Return ONLY JSON:

{{
  "R001": {{"verdict": "PASS", "evidence": "reason"}}
}}

Rules:
- PASS = correct
- FAIL = incorrect
- UNCLEAR = not visible

IMPORTANT:
- Include ALL rules
- No text outside JSON
"""
        },
        {
            "type": "image_url",
            "image_url": {"url": f"data:image/png;base64,{ref_b64}"}
        }
    ] + page_images

    response = llm.invoke([{"role": "user", "content": message}])
    raw = response.content.strip()

    print("\n--- CLAUDE RAW ---\n", raw[:800])

    raw = raw.replace("```json", "").replace("```", "").strip()

    match = re.search(r"\{.*\}", raw, re.DOTALL)
    if not match:
        raise ValueError(f"No JSON from Claude:\n{raw}")

    verdicts = json.loads(match.group())

    results = []
    for rule_id, rule in rules:
        v = verdicts.get(rule_id, {})
        results.append({
            "rule_id": rule_id,
            "rule_text": rule["rule"],
            "verdict": v.get("verdict", "UNCLEAR"),
            "evidence": v.get("evidence", "")
        })

    return results

# =========================
# BATCHING
# =========================
def batch_rules(rule_map):
    groups = {}
    for rule_id, rule in rule_map.items():
        key = rule["image"]
        groups.setdefault(key, []).append((rule_id, rule))
    return [{"image": k, "rules": v} for k, v in groups.items()]

# =========================
# REPORT
# =========================
def generate_report(results, output):
    doc = SimpleDocTemplate(str(output), pagesize=A4)
    styles = getSampleStyleSheet()
    story = [Paragraph("QA Report", styles["Title"])]

    for r in results:
        story.append(Paragraph(f"{r['rule_id']} - {r['verdict']}", styles["Normal"]))

    doc.build(story)

# =========================
# 🔥 FASTAPI ENTRY
# =========================
def run_and_return(pdf_path, checklist_path):
    pdf_path = Path(pdf_path)

    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    rule_map = load_rules_from_excel(checklist_path)
    pages = pdf_to_images(pdf_path)

    results = check_text_rules(pdf_path)

    batches = batch_rules(rule_map)

    for batch in batches:
        results.extend(check_batch(batch, pages))

    job_path = pdf_path.parent

    with open(job_path / "reference_validation_results.json", "w") as f:
        json.dump(results, f, indent=2)

    generate_report(results, job_path / "reference_validation_report.pdf")

    return results