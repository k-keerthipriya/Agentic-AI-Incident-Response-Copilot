
from fastapi import FastAPI, UploadFile, File, HTTPException
import csv
import io

from app.detection import detect_threats
from app.reporting import generate_report

app = FastAPI(
    title="Agentic AI Incident Response Copilot",
    description="Cybersecurity incident investigation API",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "project": "Agentic AI Incident Response Copilot",
        "status": "running"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/upload")
async def upload_logs(file: UploadFile = File(...)):

    if not file.filename.lower().endswith(".csv"):
        raise HTTPException(
            status_code=400,
            detail="Please upload a CSV file"
        )

    content = await file.read()

    try:
        rows = list(
            csv.DictReader(
                io.StringIO(content.decode("utf-8-sig"))
            )
        )
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Unable to read CSV file"
        )

    if not rows:
        raise HTTPException(
            status_code=400,
            detail="CSV file contains no records"
        )

    findings = detect_threats(rows)

    return generate_report(rows, findings)
