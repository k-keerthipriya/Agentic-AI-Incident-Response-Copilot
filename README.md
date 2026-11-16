
# Agentic AI Incident Response Copilot

A Python-based cybersecurity tool that analyses security event logs, identifies suspicious activity, and generates incident investigation reports.

## Features

- Upload security logs in CSV format
- Detect repeated failed login attempts
- Identify suspicious PowerShell execution
- Detect possible privilege escalation
- Flag unusually large outbound data transfers
- Generate a security incident report with severity levels
- Provide recommended investigation actions

## Technology Stack

- Python
- FastAPI
- CSV processing
- Uvicorn
- Pytest

## Project Structure

```text
Agentic-AI-Incident-Response-Copilot/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── detection.py
│   └── reporting.py
│
├── data/
│   └── sample_security_logs.csv
│
└── requirements.txt
```

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
uvicorn app.main:app --reload
```

Open the API documentation:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Project status |
| GET | `/health` | Health check |
| POST | `/upload` | Analyse uploaded CSV logs |

## Future Enhancements

- LLM-powered incident investigation
- LangGraph-based agent workflows
- RAG-based cybersecurity knowledge retrieval
- MITRE ATT&CK mapping
- Automated incident response recommendations
- MCP integration

## Disclaimer

This project is an educational prototype. Detection results are advisory and require human verification.
