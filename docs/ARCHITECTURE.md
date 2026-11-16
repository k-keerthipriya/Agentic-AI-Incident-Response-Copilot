# Project Architecture

## Workflow

1. User uploads a CSV security log file.
2. FastAPI receives and reads the file.
3. The detection module analyses security events.
4. Suspicious activities are identified using detection rules.
5. The reporting module calculates overall severity.
6. The API returns a structured incident report.

## Main Components

- `main.py`: API endpoints and file upload handling.
- `detection.py`: Security event detection rules.
- `reporting.py`: Incident report generation.
- `sample_security_logs.csv`: Sample test data.

## Future Architecture

The project can be extended with LangGraph agents, LLM-based investigation, RAG, and MITRE ATT&CK mapping.
