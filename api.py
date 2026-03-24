import uuid
import threading
import shutil
from pathlib import Path
from datetime import datetime

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from reference_validator import run_and_return

# =========================
# INIT
# =========================
app = FastAPI()

# 🔥 CORS (frontend compatibility)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten later if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# CONFIG
# =========================
BASE_DIR = Path(__file__).parent
UPLOAD_DIR = BASE_DIR / "drawings"
UPLOAD_DIR.mkdir(exist_ok=True)

CHECKLIST_PATH = BASE_DIR / "reference_images" / "Optus_DFC_Checklist.xlsx"

jobs = {}

# =========================
# BACKGROUND JOB
# =========================
def run_job(job_id: str, file_path: Path):
    try:
        jobs[job_id]["status"] = "running"

        results = run_and_return(file_path, CHECKLIST_PATH)

        # 🔥 Summary calculation
        pass_count = sum(1 for r in results if r["verdict"] == "PASS")
        fail_count = sum(1 for r in results if r["verdict"] == "FAIL")
        unclear_count = sum(1 for r in results if r["verdict"] == "UNCLEAR")

        jobs[job_id]["status"] = "complete"
        jobs[job_id]["results"] = results
        jobs[job_id]["summary"] = {
            "pass": pass_count,
            "fail": fail_count,
            "unclear": unclear_count,
            "total": len(results)
        }

    except Exception as e:
        jobs[job_id]["status"] = "failed"
        jobs[job_id]["error"] = str(e)

# =========================
# VALIDATE (ENTRY POINT)
# =========================
@app.post("/validate")
async def validate(pdf_file: UploadFile = File(...)):
    job_id = str(uuid.uuid4())[:8]

    file_path = UPLOAD_DIR / f"{job_id}_{pdf_file.filename}"

    # Save uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(pdf_file.file, buffer)

    # Initialize job
    jobs[job_id] = {
        "status": "queued",
        "file": pdf_file.filename,
        "started_at": datetime.now().isoformat(),
        "results": [],
        "summary": {}
    }

    # Run in background
    thread = threading.Thread(
        target=run_job,
        args=(job_id, file_path)
    )
    thread.start()

    return {
        "job_id": job_id,
        "status": "queued"
    }

# =========================
# STATUS
# =========================
@app.get("/status/{job_id}")
def get_status(job_id: str):
    if job_id not in jobs:
        return {"error": "Job not found"}
    return jobs[job_id]

# =========================
# RESULTS
# =========================
@app.get("/results/{job_id}")
def get_results(job_id: str):
    job = jobs.get(job_id)

    if not job:
        return {"error": "Job not found"}

    if job["status"] != "complete":
        return {"error": "Job not completed"}

    return job["results"]

# =========================
# REPORT (SUMMARY + RESULTS)
# =========================
@app.get("/report/{job_id}")
def get_report(job_id: str):
    job = jobs.get(job_id)

    if not job:
        return {"error": "Job not found"}

    if job["status"] != "complete":
        return {"error": "Job not completed"}

    return {
        "summary": job["summary"],
        "results": job["results"]
    }

# =========================
# HEALTH CHECK
# =========================
@app.get("/health")
def health():
    return {"status": "ok"}