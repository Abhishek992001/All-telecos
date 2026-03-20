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
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.enums import TA_CENTER
from knowledge_base import init_kb, update_knowledge_base, query_knowledge_base, print_kb_summary
 
load_dotenv()
 
# ── Config ────────────────────────────────────────────────
REFERENCE_DIR       = Path("reference_images")
ANTHROPIC_API_KEY   = os.getenv("ANTHROPIC_API_KEY")
RETRY_LIMIT         = 5
RETRY_DELAY         = 30
SLEEP_BETWEEN_RULES = 20
 
# ── Model ─────────────────────────────────────────────────
llm = ChatAnthropic(
    model="claude-sonnet-4-6",
    api_key=ANTHROPIC_API_KEY,
    max_tokens=1024
)
 
# ── Sheet → PDF page mapping ──────────────────────────────
SHEET_PAGE_MAP = {
    "general":    [0, 1, 2],
    "cover":      [0, 1],
    "site plan":  [3, 4],
    "antenna":    [5, 6, 7, 8, 9],
    "structural": [13, 14, 15, 16],
    "electrical": [17, 18, 19],
}
DEFAULT_PAGES = [0, 1, 2]
 
 
# ── Image scanner — no hardcoding ────────────────────────
def get_available_images() -> dict:
    """
    Scans reference_images/ folder and builds a map of
    lowercase filename stem → actual filename.
    Works with whatever PNGs exist — no hardcoding needed.
    """
    image_map = {}
    for png in REFERENCE_DIR.glob("*.png"):
        key = png.stem.lower().strip()
        image_map[key] = png.name
    return image_map
 
 
# ── Excel parser ──────────────────────────────────────────
def load_rules_from_excel(excel_path: str) -> dict:
    """
    Parses Optus DFC checklist Excel.
    Columns used:
        Col 2 → Sheet name
        Col 3 → Check points (rule text)
        Col 4 → Explanation
        Col 5 → Image reference
 
    Matches image column text against PNGs in reference_images/.
    Only includes rules that have a matching PNG.
    """
    available_images = get_available_images()
    print(f"  Found {len(available_images)} reference images: "
          f"{list(available_images.values())}")
 
    wb = openpyxl.load_workbook(excel_path)
    ws = wb.active
 
    rule_map      = {}
    rule_counter  = 1
    current_sheet = "general"
 
    for row in ws.iter_rows(min_row=2, values_only=True):
        sheet_name  = row[1]
        check_point = row[2]
        explanation = row[3]
        image_ref   = row[4]
 
        # Update current sheet context
        if sheet_name and str(sheet_name).strip():
            current_sheet = str(sheet_name).strip().lower()
 
        # Skip rows with no check point
        if not check_point or str(check_point).strip() == "":
            continue
 
        check_point = str(check_point).strip()
        explanation = str(explanation).strip() if explanation else ""
        image_ref   = str(image_ref).strip()   if image_ref   else ""
 
        # ── Match image ref to available PNGs ─────────────
        matched_image = None
        if image_ref and image_ref.lower() not in ["none", "nan", ""]:
 
            # Extract quoted text e.g. "1-scale" from Refer "1-scale" image
            quoted = re.findall(r'"([^"]+)"', image_ref)
 
            for q in quoted:
                q_lower = q.lower().strip()
 
                # Direct match
                if q_lower in available_images:
                    matched_image = available_images[q_lower]
                    break
 
                # Partial match
                for key, filename in available_images.items():
                    if q_lower in key or key in q_lower:
                        matched_image = filename
                        break
 
                if matched_image:
                    break
 
            # Fallback — search full image_ref string
            if not matched_image:
                ref_lower = image_ref.lower()
                for key, filename in available_images.items():
                    if key in ref_lower:
                        matched_image = filename
                        break
 
        # Skip rules with no matching reference image
        if not matched_image:
            continue
 
        # ── Map sheet to PDF pages ────────────────────────
        pages = DEFAULT_PAGES
        for keyword, page_nums in SHEET_PAGE_MAP.items():
            if keyword in current_sheet:
                pages = page_nums
                break
 
        rule_id = f"R{str(rule_counter).zfill(3)}"
 
        rule_map[rule_id] = {
            "rule":        check_point,
            "image":       matched_image,
            "check":       f"Check this rule against the reference image: {check_point}",
            "explanation": explanation,
            "pages":       pages,
            "sheet":       current_sheet,
        }
 
        rule_counter += 1
 
    print(f"  Loaded {len(rule_map)} rules with reference images from checklist")
    return rule_map
 
 
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
 
 
# ── Core validation function ──────────────────────────────
def check_rule_against_reference_fn(rule_id: str, pdf_path: str,
                                     rule_map: dict) -> str:
    """
    Checks knowledge base first.
    Falls back to Claude if not cached.
    Returns JSON with rule_id, rule_text, verdict, evidence.
    """
    if rule_id not in rule_map:
        return json.dumps({
            "rule_id":  rule_id,
            "verdict":  "UNCLEAR",
            "evidence": "Rule not found in checklist"
        })
 
    rule = rule_map[rule_id]
 
    # ── Check knowledge base first ────────────────────────
    cached = query_knowledge_base(rule_id)
    if cached:
        print(f"  📚 {rule_id} from knowledge base "
              f"(confidence: {cached['confidence']:.2f})")
        cached["rule_id"]   = rule_id
        cached["rule_text"] = rule["rule"]
        return json.dumps(cached)
 
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
                if "rate" in str(e).lower() or "529" in str(e) or \
                   "overloaded" in str(e).lower():
                    print(f"  ⏳ Rate limited — waiting {RETRY_DELAY}s "
                          f"(attempt {attempt+1}/{RETRY_LIMIT})")
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
    doc    = SimpleDocTemplate(output_file, pagesize=A4,
                               rightMargin=15*mm, leftMargin=15*mm,
                               topMargin=20*mm,   bottomMargin=20*mm)
    styles = getSampleStyleSheet()
    story  = []
 
    title_style = ParagraphStyle("title", parent=styles["Title"],
                                  fontSize=18, textColor=colors.HexColor("#1a1a2e"),
                                  spaceAfter=6)
    sub_style   = ParagraphStyle("sub", parent=styles["Normal"],
                                  fontSize=10, textColor=colors.grey, spaceAfter=2)
    cell_style  = ParagraphStyle("cell", parent=styles["Normal"],
                                  fontSize=8, leading=11)
 
    story.append(Paragraph("Telecom Drawing QA Report", title_style))
    story.append(Paragraph(f"Drawing: {Path(pdf_path).name}", sub_style))
    story.append(Paragraph(f"Generated: {time.strftime('%d %B %Y %H:%M')}", sub_style))
    story.append(Paragraph("Company: DLUX Tech", sub_style))
    story.append(Spacer(1, 8*mm))
 
    pass_count    = sum(1 for r in results if r["verdict"] == "PASS")
    fail_count    = sum(1 for r in results if r["verdict"] == "FAIL")
    unclear_count = sum(1 for r in results if r["verdict"] == "UNCLEAR")
 
    summary_table = Table(
        [["PASS", "FAIL", "UNCLEAR", "TOTAL"],
         [str(pass_count), str(fail_count), str(unclear_count), str(len(results))]],
        colWidths=[40*mm, 40*mm, 40*mm, 40*mm]
    )
    summary_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1a1a2e")),
        ("TEXTCOLOR",  (0, 0), (-1, 0), colors.white),
        ("FONTNAME",   (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",   (0, 0), (-1,-1), 11),
        ("ALIGN",      (0, 0), (-1,-1), "CENTER"),
        ("VALIGN",     (0, 0), (-1,-1), "MIDDLE"),
        ("ROWHEIGHT",  (0, 0), (-1,-1), 10*mm),
        ("BACKGROUND", (0, 1), (0, 1),  colors.HexColor("#d4edda")),
        ("BACKGROUND", (1, 1), (1, 1),  colors.HexColor("#f8d7da")),
        ("BACKGROUND", (2, 1), (2, 1),  colors.HexColor("#fff3cd")),
        ("BACKGROUND", (3, 1), (3, 1),  colors.HexColor("#e2e3e5")),
        ("FONTNAME",   (0, 1), (-1, 1), "Helvetica-Bold"),
        ("FONTSIZE",   (0, 1), (-1, 1), 14),
        ("GRID",       (0, 0), (-1,-1), 0.5, colors.grey),
    ]))
    story.append(summary_table)
    story.append(Spacer(1, 8*mm))
 
    story.append(Paragraph("Detailed Results",
                 ParagraphStyle("section", parent=styles["Heading2"],
                                fontSize=13, textColor=colors.HexColor("#1a1a2e"),
                                spaceAfter=4)))
    story.append(Spacer(1, 3*mm))
 
    table_data = [["ID", "Rule", "Verdict", "Evidence"]]
    for r in results:
        verdict = r.get("verdict", "UNCLEAR")
        table_data.append([
            Paragraph(r.get("rule_id",   ""), cell_style),
            Paragraph(r.get("rule_text", ""), cell_style),
            Paragraph(verdict,                cell_style),
            Paragraph(r.get("evidence",  ""), cell_style),
        ])
 
    results_table = Table(table_data, colWidths=[15*mm, 45*mm, 22*mm, 93*mm])
 
    style_cmds = [
        ("BACKGROUND",   (0,0), (-1,0), colors.HexColor("#1a1a2e")),
        ("TEXTCOLOR",    (0,0), (-1,0), colors.white),
        ("FONTNAME",     (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE",     (0,0), (-1,-1), 8),
        ("ALIGN",        (0,0), (-1,0), "CENTER"),
        ("VALIGN",       (0,0), (-1,-1), "TOP"),
        ("GRID",         (0,0), (-1,-1), 0.4, colors.HexColor("#cccccc")),
        ("TOPPADDING",   (0,0), (-1,-1), 4),
        ("BOTTOMPADDING",(0,0), (-1,-1), 4),
        ("LEFTPADDING",  (0,0), (-1,-1), 4),
    ]
    for i, r in enumerate(results, start=1):
        verdict = r.get("verdict", "UNCLEAR")
        if i % 2 == 0:
            style_cmds.append(("BACKGROUND", (0,i), (1,i), colors.HexColor("#f9f9f9")))
            style_cmds.append(("BACKGROUND", (3,i), (3,i), colors.HexColor("#f9f9f9")))
        if verdict == "PASS":
            style_cmds.append(("BACKGROUND", (2,i), (2,i), colors.HexColor("#d4edda")))
            style_cmds.append(("TEXTCOLOR",  (2,i), (2,i), colors.HexColor("#155724")))
            style_cmds.append(("FONTNAME",   (2,i), (2,i), "Helvetica-Bold"))
        elif verdict == "FAIL":
            style_cmds.append(("BACKGROUND", (2,i), (2,i), colors.HexColor("#f8d7da")))
            style_cmds.append(("TEXTCOLOR",  (2,i), (2,i), colors.HexColor("#721c24")))
            style_cmds.append(("FONTNAME",   (2,i), (2,i), "Helvetica-Bold"))
        else:
            style_cmds.append(("BACKGROUND", (2,i), (2,i), colors.HexColor("#fff3cd")))
            style_cmds.append(("TEXTCOLOR",  (2,i), (2,i), colors.HexColor("#856404")))
            style_cmds.append(("FONTNAME",   (2,i), (2,i), "Helvetica-Bold"))
 
    results_table.setStyle(TableStyle(style_cmds))
    story.append(results_table)
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph(
        f"Generated by DLUX Tech QA System — {time.strftime('%d %B %Y %H:%M')}",
        ParagraphStyle("footer", parent=styles["Normal"],
                       fontSize=8, textColor=colors.grey, alignment=TA_CENTER)
    ))
    doc.build(story)
    print(f"\n  PDF report saved to: {output_file}")
 
 
# ── Validation pipeline ───────────────────────────────────
def run_reference_validation(pdf_path: str, checklist_path: str):
    print("\n================================================")
    print("  TELECOM DRAWING QA VALIDATOR")
    print("================================================\n")
 
    if not Path(pdf_path).exists():
        print("PDF not found:", pdf_path)
        return
 
    if not Path(checklist_path).exists():
        print("Checklist not found:", checklist_path)
        return
 
    print("Parsing checklist...")
    rule_map = load_rules_from_excel(checklist_path)
 
    if not rule_map:
        print("No rules with reference images found.")
        return
 
    results = []
 
    for rule_id, rule in rule_map.items():
        print(f"\nChecking {rule_id} — {rule['rule'][:60]}...")
 
        output = check_rule_against_reference_fn(rule_id, pdf_path, rule_map)
        parsed = json.loads(output)
        results.append(parsed)
 
        verdict  = parsed.get("verdict", "UNCLEAR")
        evidence = parsed.get("evidence", "")[:80]
 
        if verdict == "PASS":
            print(f"  ✅ PASS — {evidence}")
        elif verdict == "FAIL":
            print(f"  ❌ FAIL — {evidence}")
        else:
            print(f"  ⚠️  UNCLEAR — {evidence}")
 
        if parsed.get("source") != "knowledge_base":
            print(f"  Waiting {SLEEP_BETWEEN_RULES}s...")
            time.sleep(SLEEP_BETWEEN_RULES)
 
    # ── Save JSON ─────────────────────────────────────────
    json_file = "reference_validation_results.json"
    with open(json_file, "w") as f:
        json.dump(results, f, indent=2)
 
    # ── Generate PDF ──────────────────────────────────────
    pdf_file = "reference_validation_report.pdf"
    generate_pdf_report(results, pdf_path, pdf_file)
 
    # ── Update knowledge base ─────────────────────────────
    update_knowledge_base(results, pdf_path, rule_map)
    print_kb_summary()
 
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
 
 
def run_and_return(pdf_path: str, checklist_path: str) -> list:
    if not Path(pdf_path).exists():
        return []
 
    rule_map = load_rules_from_excel(checklist_path)
    results  = []
 
    for rule_id in rule_map.keys():
        output = check_rule_against_reference_fn(rule_id, pdf_path, rule_map)
        parsed = json.loads(output)
        results.append(parsed)
 
        if parsed.get("source") != "knowledge_base":
            time.sleep(SLEEP_BETWEEN_RULES)
 
    update_knowledge_base(results, pdf_path, rule_map)
    print_kb_summary()
 
    return results
 
 
# ── Entry point ───────────────────────────────────────────
if __name__ == "__main__":
    import sys
 
    if len(sys.argv) < 3:
        print("\nUsage:")
        print("  python reference_validator.py <pdf_path> <checklist_path>\n")
        print("Example:")
        print("  python reference_validator.py "
              "drawings/M8398.pdf "
              "C:/path/to/Optus_DFC_Checklist.xlsx\n")
        sys.exit(1)
 
    run_reference_validation(sys.argv[1], sys.argv[2])
 