import pandas as pd
import json
import time
from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

# ─────────────────────────────
# Load rules from Excel
# ─────────────────────────────
def load_rules_from_excel(excel_path):
    df = pd.read_excel(excel_path)

    rules = {}
    for _, row in df.iterrows():
        rules[row['rule_id']] = {
            "rule": str(row['rule']),
            "check": str(row['check']),
            "explanation": str(row['explanation']),
            "pages": [int(p) for p in str(row['pages']).split(',')]
        }

    return rules


# ─────────────────────────────
# Dummy validation (replace with AI logic)
# ─────────────────────────────
def check_rule(rule, pdf_path):
    return {
        "verdict": "PASS" if "scale" in rule["rule"].lower() else "FAIL",
        "evidence": "Auto-checked result"
    }


# ─────────────────────────────
# Run validation
# ─────────────────────────────
def run_validation(pdf_path, rules):
    results = []

    for rule_id, rule in rules.items():
        print(f"Checking {rule_id}...")

        result = check_rule(rule, pdf_path)

        results.append({
            "rule_id": rule_id,
            "rule_text": rule["rule"],
            "verdict": result["verdict"],
            "evidence": result["evidence"]
        })

        time.sleep(1)

    return results


# ─────────────────────────────
# Generate PDF report
# ─────────────────────────────
def generate_pdf(results, output_file):
    doc = SimpleDocTemplate(output_file, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("PDF Validation Report", styles['Title']))
    story.append(Spacer(1, 10))

    data = [["Rule ID", "Rule", "Verdict", "Evidence"]]

    for r in results:
        data.append([
            r["rule_id"],
            r["rule_text"],
            r["verdict"],
            r["evidence"]
        ])

    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
    ]))

    story.append(table)
    doc.build(story)

    print("✅ PDF generated:", output_file)


# ─────────────────────────────
# MAIN
# ─────────────────────────────
if __name__ == "__main__":
    pdf_path = r"C:\Users\AbhishekP\reference_validator\drawings\M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf"
    excel_path = r"C:\Users\AbhishekP\reference_validator\reference_images\Optus_DFC_Checklist_12012026.xlsx"

    rules = load_rules_from_excel(excel_path)
    results = run_validation(pdf_path, rules)

    generate_pdf(results, "report.pdf")