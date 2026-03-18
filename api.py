import sys
import uuid
import threading
from pathlib import Path
from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel

sys.path.append(str(Path(__file__).parent))

from reference_validator import run_reference_validation, run_and_return

app  = FastAPI()
jobs = {}


class ValidateRequest(BaseModel):
    pdf_filename: str


def run_job(job_id: str, pdf_path: str):
    try:
        jobs[job_id]["status"] = "running"

        # run_reference_validation returns results
        # we need to modify it slightly to return results
        results = run_and_return(pdf_path)

        jobs[job_id]["status"]  = "complete"
        jobs[job_id]["results"] = results

        pass_count    = sum(1 for r in results if r["verdict"] == "PASS")
        fail_count    = sum(1 for r in results if r["verdict"] == "FAIL")
        unclear_count = sum(1 for r in results if r["verdict"] == "UNCLEAR")

        jobs[job_id]["summary"] = {
            "pass":    pass_count,
            "fail":    fail_count,
            "unclear": unclear_count,
            "total":   len(results)
        }

    except Exception as e:
        jobs[job_id]["status"] = "failed"
        jobs[job_id]["error"]  = str(e)


@app.post("/validate")
def validate(req: ValidateRequest):
    job_id   = str(uuid.uuid4())[:8]
    pdf_path = str(Path(__file__).parent / "drawings" / req.pdf_filename)

    jobs[job_id] = {
        "status":     "queued",
        "pdf":        req.pdf_filename,
        "started_at": datetime.now().isoformat(),
        "results":    [],
        "summary":    {}
    }

    thread = threading.Thread(
        target=run_job,
        args=(job_id, pdf_path)
    )
    thread.start()

    return {"job_id": job_id, "status": "queued"}


@app.get("/status/{job_id}")
def status(job_id: str):
    if job_id not in jobs:
        return {"error": "Job not found"}
    return jobs[job_id]


@app.get("/health")
def health():
    return {"status": "ok"}