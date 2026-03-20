import os
import json
import base64
import io
import re
import time
from pathlib import Path
from PIL import Image
import fitz
import openpyxl
from dotenv import load_dotenv

from langchain_anthropic import ChatAnthropic
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

load_dotenv()

# ── CONFIG ───────────────────────────
REFERENCE_DIR = Path("reference_images")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
SLEEP_BETWEEN_RULES = 1

# ── MODEL ────────────────────────────
llm = ChatAnthropic(
    model="claude-sonnet-4-6",
    api_key=ANTHROPIC_API_KEY,
    max_tokens=1024
)

# ── PAGE MAP ─────────────────────────
SHEET_PAGE_MAP = {
    "general": [0, 1, 2],
    "cover": [0, 1],
    "site plan": [3, 4],
    "antenna": [5, 6, 7],
    "structural": [13, 14],
}
DEFAULT_PAGES = [0, 1]


# ── LOAD IMAGES ──────────────────────
def get_available_images():
    image_map = {}
    for png in REFERENCE_DIR.glob("*.png"):
        image_map[png.stem.lower()] = png.name
    return image_map


# ── LOAD RULES FROM EXCEL ────────────
def load_rules_from_excel(excel_path):
    available_images = get_available_images()
    wb = openpyxl.load_workbook(excel_path)
    ws = wb.active

    rule_map = {}
    rule_counter = 1
    current_sheet = "general"

    for row in ws.iter_rows(min_row=2, values_only=True):
        sheet_name = row[1]
        check_point = row[2]
        explanation = row[3]
        image_ref = row[4]

        if sheet_name:
            current_sheet = str(sheet_name).lower()

        if not check_point:
            continue

        check_point = str(check_point)
        explanation = str(explanation or "")
        image_ref = str(image_ref or "")

        # match image (optional)
        matched_image = None
        for key, filename in available_images.items():
            if key in image_ref.lower():
                matched_image = filename
                break

        # page mapping
        pages = DEFAULT_PAGES
        for k, v in SHEET_PAGE_MAP.items():
            if k in current_sheet:
                pages = v

        rule_id = f"R{str(rule_counter).zfill(3)}"

        rule_map[rule_id] = {
            "rule": check_point,
            "image": matched_image,
            "explanation": explanation,
            "pages": pages,
        }

        rule_counter += 1

    print(f"Loaded {len(rule_map)} rules")
    return rule_map


# ── HELPERS ──────────────────────────
def image_to_base64(image):
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode()


def pdf_to_images(pdf_path):
    images = []
    doc = fitz.open(pdf_path)
    for page in doc:
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        images.append(img)
    doc.close()
    return images


# ── MAIN VALIDATION ──────────────────
def check_rule(rule_id, pdf_path, rule_map):

    rule = rule_map[rule_id]

    try:
        doc = fitz.open(pdf_path)

        # 🔥 Extract TEXT
        extracted_text = ""
        for i in rule["pages"]:
            if i < len(doc):
                extracted_text += doc[i].get_text()

        is_empty = len(extracted_text.strip()) < 10

        # 🔥 Convert pages to images
        all_pages = pdf_to_images(pdf_path)
        pages = [all_pages[i] for i in rule["pages"] if i < len(all_pages)]

        page_images = [
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/png;base64,{image_to_base64(p)}"
                }
            }
            for p in pages
        ]

        # 🔥 COMMON PROMPT
        prompt = f"""
You are a telecom QA engineer.

Rule: {rule['rule']}
Explanation: {rule['explanation']}

Extracted Text:
{extracted_text[:2000]}

Check strictly:
- Missing data
- Wrong values
- Empty sections

Return ONLY JSON:
{{"verdict":"PASS/FAIL/UNCLEAR","evidence":"reason"}}
"""

        # 🔥 EMPTY DETECTION
        if is_empty:
            return {
                "rule_id": rule_id,
                "rule_text": rule["rule"],
                "verdict": "FAIL",
                "evidence": "No content found in PDF"
            }

        # 🔥 WITH IMAGE
        if rule["image"]:
            ref_img = Image.open(REFERENCE_DIR / rule["image"])
            ref_b64 = image_to_base64(ref_img)

            message = [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{ref_b64}"}}
            ] + page_images

        # 🔥 WITHOUT IMAGE
        else:
            message = [{"type": "text", "text": prompt}] + page_images

        # 🔥 CALL AI
        response = llm.invoke([{"role": "user", "content": message}])
        raw = response.content.strip()

        match = re.search(r'\{.*\}', raw, re.DOTALL)

        if match:
            result = json.loads(match.group())
        else:
            result = {
                "verdict": "UNCLEAR",
                "evidence": raw[:200]
            }

        result["rule_id"] = rule_id
        result["rule_text"] = rule["rule"]

        return result

    except Exception as e:
        return {
            "rule_id": rule_id,
            "rule_text": rule["rule"],
            "verdict": "UNCLEAR",
            "evidence": str(e)
        }


# ── PDF REPORT ───────────────────────
def generate_pdf(results, output):

    if not results:
        print("❌ No results")
        return

    doc = SimpleDocTemplate(output, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("QA Validation Report", styles["Title"]))
    story.append(Spacer(1, 10))

    data = [["Rule ID", "Rule", "Verdict", "Evidence"]]

    for r in results:
        data.append([
            r["rule_id"],
            r["rule_text"],
            r["verdict"],
            r["evidence"]
        ])

    table = Table(data, repeatRows=1)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.black),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('FONTSIZE', (0,0), (-1,-1), 8),
    ]))

    story.append(table)
    doc.build(story)

    print("✅ PDF generated:", output)


# ── RUN ──────────────────────────────
def run(pdf_path, excel_path):

    rule_map = load_rules_from_excel(excel_path)

    results = []
    for rule_id in rule_map:
        print("Checking", rule_id)
        res = check_rule(rule_id, pdf_path, rule_map)
        results.append(res)

    generate_pdf(results, "report.pdf")


# ── ENTRY ────────────────────────────
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: python script.py <pdf> <excel>")
        exit()

    run(sys.argv[1], sys.argv[2])