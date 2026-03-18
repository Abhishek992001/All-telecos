import os
import json
import base64
import io
import time
from pathlib import Path
from PIL import Image
import fitz
from dotenv import load_dotenv
import re 

from langchain_anthropic import ChatAnthropic
from langchain.tools import tool
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.enums import TA_CENTER

load_dotenv()

# ── Config ────────────────────────────────────────────────
REFERENCE_DIR       = Path("reference_images")
ANTHROPIC_API_KEY   = os.getenv("ANTHROPIC_API_KEY")
RETRY_LIMIT         = 5
RETRY_DELAY         = 20
SLEEP_BETWEEN_RULES = 12

# ── Rule definitions ──────────────────────────────────────
RULE_IMAGE_MAP = {
    "R002": {
        "rule":        "Drawings must be correct scale in all sheets",
        "image":       "1-Scale.png",
        "check":       "Verify drawing scale follows the standard scale shown in the reference.",
        "explanation": "Check all drawing scale with standard scale. If scale is not followed the standard or acceptable, need to highlight.",
        "pages":       [3, 4, 5]
    },
    "R003": {
        "rule":        "Check scale with viewport",
        "image":       "1-SCALE & Viewport.png",
        "check":       "Ensure drawing scale matches viewport scale shown in the reference.",
        "explanation": "Check shown scale must be a standard one. Also scale must be matched with viewport.",
        "pages":       [3, 4, 5]
    },
    "R004": {
        "rule":        "FC stamp correctly mentioned",
        "image":       "2-Draft.png",
        "check":       "Verify the FOR CONSTRUCTION stamp exists in the sheet.",
        "explanation": "Draft symbol must be in all sheets.",
        "pages":       [0, 3, 7, 13, 17]
    },
    "R005": {
        "rule":        "Layers correctly followed",
        "image":       "3-Optus FC template Layer format.png",
        "check":       "Existing elements should be unbold while proposed elements should be bold.",
        "explanation": "Main objective is existing must be in unbold layer whereas proposed must be in bold layer.",
        "pages":       [3, 4, 5]
    },
    "R005b": {
        "rule":        "Child CAD template layer format",
        "image":       "4-Child CAD template Layer format.png",
        "check":       "Layer names and formatting should follow the child CAD template.",
        "explanation": "Main objective is existing must be in unbold layer whereas proposed must be in bold layer. You can find the layer formats in CAD template in Model space.",
        "pages":       [3, 4, 5]
    }
}

# Model
llm = ChatAnthropic(
    model="claude-sonnet-4-6",
    api_key=ANTHROPIC_API_KEY,
    max_tokens=1024
)

# Timing
RETRY_DELAY         = 30
SLEEP_BETWEEN_RULES = 20

# ── Image helpers ─────────────────────────────────────────
def image_to_base64(image: Image.Image) -> str:
    max_width = 1024
    if image.width > max_width:
        ratio  = max_width / image.width
        height = int(image.height * ratio)
        image  = image.resize((max_width, height))
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode("utf-8")


def load_reference_image(filename: str) -> Image.Image:
    path = REFERENCE_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"Reference image not found: {path}")
    return Image.open(path).convert("RGB")


def pdf_to_images(pdf_path: str, dpi: int = 150) -> list:
    images = []
    doc    = fitz.open(pdf_path)
    zoom   = dpi / 72
    matrix = fitz.Matrix(zoom, zoom)
    for page in doc:
        pix = page.get_pixmap(matrix=matrix)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        images.append(img)
    doc.close()
    return images


# ── Tool ──────────────────────────────────────────────────
@tool
def check_rule_against_reference(rule_id: str, pdf_path: str) -> str:
    """
    Compares FC drawing pages against a reference standard image
    and determines if the drawing follows the rule.

    Returns JSON containing rule_id, rule_text, verdict (PASS/FAIL/UNCLEAR), evidence.
    """

    if rule_id not in RULE_IMAGE_MAP:
        return json.dumps({
            "rule_id":  rule_id,
            "verdict":  "UNCLEAR",
            "evidence": "Rule not configured"
        })

    rule = RULE_IMAGE_MAP[rule_id]

    try:
        ref_img = load_reference_image(rule["image"])
        ref_b64 = image_to_base64(ref_img)

        all_pages    = pdf_to_images(pdf_path)
        page_numbers = rule.get("pages", [0])
        pages        = [all_pages[i] for i in page_numbers if i < len(all_pages)]

        page_images = [
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/png;base64,{image_to_base64(p)}"
                }
            }
            for p in pages
        ]

        message = [
            {
                "type": "text",
                "text": f"""You are a telecom drawing QA engineer checking an Optus FC drawing.

Rule to check: {rule['rule']}
What to check: {rule['check']}
Explanation:   {rule['explanation']}

You will be shown:
1. Reference image — shows what a CORRECT drawing looks like
2. FC drawing pages — the drawing being checked

Compare them and return ONLY a JSON object, no other text:
{{"verdict": "PASS", "evidence": "what you found"}}

Use only PASS, FAIL, or UNCLEAR for verdict."""
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/png;base64,{ref_b64}"
                }
            },
            {
                "type": "text",
                "text": "Above is the REFERENCE image. Below are the FC drawing pages to check:"
            }
        ] + page_images

        for attempt in range(RETRY_LIMIT):
            try:
                response = llm.invoke([{"role": "user", "content": message}])
                raw      = response.content.strip()
                raw      = raw.replace("```json", "").replace("```", "").strip()

                # ── Extract JSON even if model adds extra text ────
                match = re.search(r'\{.*\}', raw, re.DOTALL)
                if match:
                    result = json.loads(match.group())
                else:
                    result = {
                        "verdict":  "UNCLEAR",
                        "evidence": raw[:300] if raw else "Empty response"
                    }

                result["rule_id"]   = rule_id
                result["rule_text"] = rule["rule"]
                return json.dumps(result)

            except Exception as e:
                if "rate" in str(e).lower() or "529" in str(e) or "overloaded" in str(e).lower():
                    print(f"  ⏳ Rate limited — waiting {RETRY_DELAY}s (attempt {attempt+1}/{RETRY_LIMIT})")
                    time.sleep(RETRY_DELAY)
                else:
                    raise

        return json.dumps({
            "rule_id":   rule_id,
            "rule_text": rule["rule"],
            "verdict":   "UNCLEAR",
            "evidence":  "API rate limit retry failed after all attempts"
        })

    except Exception as e:
        return json.dumps({
            "rule_id":   rule_id,
            "rule_text": rule["rule"],
            "verdict":   "UNCLEAR",
            "evidence":  str(e)
        })
# ── PDF Report ────────────────────────────────────────────
def generate_pdf_report(results: list, pdf_path: str, output_file: str):

    doc = SimpleDocTemplate(
        output_file,
        pagesize=A4,
        rightMargin=15*mm,
        leftMargin=15*mm,
        topMargin=20*mm,
        bottomMargin=20*mm
    )

    styles = getSampleStyleSheet()
    story  = []

    # ── Header ────────────────────────────────────────────
    title_style = ParagraphStyle(
        "title",
        parent    = styles["Title"],
        fontSize  = 18,
        textColor = colors.HexColor("#1a1a2e"),
        spaceAfter= 6
    )
    sub_style = ParagraphStyle(
        "sub",
        parent    = styles["Normal"],
        fontSize  = 10,
        textColor = colors.grey,
        spaceAfter= 2
    )

    story.append(Paragraph("Telecom Drawing QA Report", title_style))
    story.append(Paragraph(f"Drawing: {Path(pdf_path).name}", sub_style))
    story.append(Paragraph(f"Generated: {time.strftime('%d %B %Y %H:%M')}", sub_style))
    story.append(Paragraph("Company: DLUX Tech", sub_style))
    story.append(Spacer(1, 8*mm))

    # ── Summary box ───────────────────────────────────────
    pass_count    = sum(1 for r in results if r["verdict"] == "PASS")
    fail_count    = sum(1 for r in results if r["verdict"] == "FAIL")
    unclear_count = sum(1 for r in results if r["verdict"] == "UNCLEAR")

    summary_data = [
        ["PASS", "FAIL", "UNCLEAR", "TOTAL"],
        [str(pass_count), str(fail_count), str(unclear_count), str(len(results))]
    ]

    summary_table = Table(summary_data, colWidths=[40*mm, 40*mm, 40*mm, 40*mm])
    summary_table.setStyle(TableStyle([
        ("BACKGROUND",  (0, 0), (-1, 0),  colors.HexColor("#1a1a2e")),
        ("TEXTCOLOR",   (0, 0), (-1, 0),  colors.white),
        ("FONTNAME",    (0, 0), (-1, 0),  "Helvetica-Bold"),
        ("FONTSIZE",    (0, 0), (-1, 0),  11),
        ("ALIGN",       (0, 0), (-1, -1), "CENTER"),
        ("VALIGN",      (0, 0), (-1, -1), "MIDDLE"),
        ("ROWHEIGHT",   (0, 0), (-1, -1), 10*mm),
        ("BACKGROUND",  (0, 1), (0, 1),   colors.HexColor("#d4edda")),
        ("BACKGROUND",  (1, 1), (1, 1),   colors.HexColor("#f8d7da")),
        ("BACKGROUND",  (2, 1), (2, 1),   colors.HexColor("#fff3cd")),
        ("BACKGROUND",  (3, 1), (3, 1),   colors.HexColor("#e2e3e5")),
        ("FONTNAME",    (0, 1), (-1, 1),  "Helvetica-Bold"),
        ("FONTSIZE",    (0, 1), (-1, 1),  14),
        ("GRID",        (0, 0), (-1, -1), 0.5, colors.grey),
    ]))

    story.append(summary_table)
    story.append(Spacer(1, 8*mm))

    # ── Results table ─────────────────────────────────────
    section_style = ParagraphStyle(
        "section",
        parent    = styles["Heading2"],
        fontSize  = 13,
        textColor = colors.HexColor("#1a1a2e"),
        spaceAfter= 4
    )
    story.append(Paragraph("Detailed Results", section_style))
    story.append(Spacer(1, 3*mm))

    cell_style = ParagraphStyle(
        "cell",
        parent  = styles["Normal"],
        fontSize= 8,
        leading = 11
    )

    header     = ["ID", "Rule", "Verdict", "Evidence"]
    table_data = [header]

    for r in results:
        verdict = r.get("verdict", "UNCLEAR")

        if verdict == "PASS":
            verdict_display = "PASS"
        elif verdict == "FAIL":
            verdict_display = "FAIL"
        else:
            verdict_display = "UNCLEAR"

        row = [
            Paragraph(r.get("rule_id", ""),   cell_style),
            Paragraph(r.get("rule_text", ""), cell_style),
            Paragraph(verdict_display,         cell_style),
            Paragraph(r.get("evidence", ""),  cell_style),
        ]
        table_data.append(row)

    results_table = Table(
        table_data,
        colWidths=[15*mm, 45*mm, 22*mm, 93*mm]
    )

    style_cmds = [
        ("BACKGROUND",   (0, 0), (-1, 0),  colors.HexColor("#1a1a2e")),
        ("TEXTCOLOR",    (0, 0), (-1, 0),  colors.white),
        ("FONTNAME",     (0, 0), (-1, 0),  "Helvetica-Bold"),
        ("FONTSIZE",     (0, 0), (-1, 0),  9),
        ("ALIGN",        (0, 0), (-1, 0),  "CENTER"),
        ("VALIGN",       (0, 0), (-1, -1), "TOP"),
        ("GRID",         (0, 0), (-1, -1), 0.4, colors.HexColor("#cccccc")),
        ("FONTSIZE",     (0, 1), (-1, -1), 8),
        ("TOPPADDING",   (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 4),
        ("LEFTPADDING",  (0, 0), (-1, -1), 4),
    ]

    for i, r in enumerate(results, start=1):
        if i % 2 == 0:
            style_cmds.append(("BACKGROUND", (0, i), (1, i), colors.HexColor("#f9f9f9")))
            style_cmds.append(("BACKGROUND", (3, i), (3, i), colors.HexColor("#f9f9f9")))

        verdict = r.get("verdict", "UNCLEAR")
        if verdict == "PASS":
            style_cmds.append(("BACKGROUND", (2, i), (2, i), colors.HexColor("#d4edda")))
            style_cmds.append(("TEXTCOLOR",  (2, i), (2, i), colors.HexColor("#155724")))
            style_cmds.append(("FONTNAME",   (2, i), (2, i), "Helvetica-Bold"))
        elif verdict == "FAIL":
            style_cmds.append(("BACKGROUND", (2, i), (2, i), colors.HexColor("#f8d7da")))
            style_cmds.append(("TEXTCOLOR",  (2, i), (2, i), colors.HexColor("#721c24")))
            style_cmds.append(("FONTNAME",   (2, i), (2, i), "Helvetica-Bold"))
        else:
            style_cmds.append(("BACKGROUND", (2, i), (2, i), colors.HexColor("#fff3cd")))
            style_cmds.append(("TEXTCOLOR",  (2, i), (2, i), colors.HexColor("#856404")))
            style_cmds.append(("FONTNAME",   (2, i), (2, i), "Helvetica-Bold"))

    results_table.setStyle(TableStyle(style_cmds))
    story.append(results_table)
    story.append(Spacer(1, 8*mm))

    # ── Footer ────────────────────────────────────────────
    footer_style = ParagraphStyle(
        "footer",
        parent    = styles["Normal"],
        fontSize  = 8,
        textColor = colors.grey,
        alignment = TA_CENTER
    )
    story.append(Paragraph(
        f"Generated by DLUX Tech QA System — {time.strftime('%d %B %Y %H:%M')}",
        footer_style
    ))

    doc.build(story)
    print(f"\n  PDF report saved to: {output_file}")


# ── Validation pipeline ───────────────────────────────────
def run_reference_validation(pdf_path: str):
    print("\n================================================")
    print("  TELECOM DRAWING QA VALIDATOR")
    print("================================================\n")

    if not Path(pdf_path).exists():
        print("PDF not found:", pdf_path)
        return

    print("Loading PDF pages...")
    results = []

    for rule_id in RULE_IMAGE_MAP.keys():
        print(f"\nChecking rule: {rule_id} — {RULE_IMAGE_MAP[rule_id]['rule']}")

        output = check_rule_against_reference.invoke({
            "rule_id":  rule_id,
            "pdf_path": pdf_path
        })

        parsed  = json.loads(output)
        results.append(parsed)

        verdict  = parsed.get("verdict", "UNCLEAR")
        evidence = parsed.get("evidence", "")[:80]

        if verdict == "PASS":
            print(f"  ✅ PASS — {evidence}")
        elif verdict == "FAIL":
            print(f"  ❌ FAIL — {evidence}")
        else:
            print(f"  ⚠️  UNCLEAR — {evidence}")

        print(f"  Waiting {SLEEP_BETWEEN_RULES}s before next rule...")
        time.sleep(SLEEP_BETWEEN_RULES)

    # ── Save JSON ─────────────────────────────────────────
    json_file = "reference_validation_results.json"
    with open(json_file, "w") as f:
        json.dump(results, f, indent=2)

    # ── Generate PDF ──────────────────────────────────────
    pdf_file = "reference_validation_report.pdf"
    generate_pdf_report(results, pdf_path, pdf_file)

    # ── Summary ───────────────────────────────────────────
    pass_count    = sum(1 for r in results if r["verdict"] == "PASS")
    fail_count    = sum(1 for r in results if r["verdict"] == "FAIL")
    unclear_count = sum(1 for r in results if r["verdict"] == "UNCLEAR")

    print("\n================================================")
    print("VALIDATION SUMMARY")
    print("================================================")
    print(f"✅ PASS    : {pass_count}")
    print(f"❌ FAIL    : {fail_count}")
    print(f"⚠️  UNCLEAR : {unclear_count}")
    print(f"\nJSON saved to : {json_file}")
    print(f"PDF saved to  : {pdf_file}")
    
def run_and_return(pdf_path: str) -> list:
    if not Path(pdf_path).exists():
        return []

    results = []

    for rule_id in RULE_IMAGE_MAP.keys():
        output = check_rule_against_reference.invoke({
            "rule_id":  rule_id,
            "pdf_path": pdf_path
        })
        parsed = json.loads(output)
        results.append(parsed)
        time.sleep(SLEEP_BETWEEN_RULES)

    return results


# ── Entry point ───────────────────────────────────────────
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("\nUsage:")
        print("  python reference_validator.py drawings/M8398.pdf\n")
        sys.exit(1)

    run_reference_validation(sys.argv[1])