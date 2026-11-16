from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_upload_csv():
    csv_content = (
        "timestamp,event_type,source_ip,username,"
        "hostname,details,bytes_out\n"
        "2026-11-16T09:00:00Z,login_failed,"
        "203.0.113.25,admin,PC01,Invalid password,0\n"
    )

    response = client.post(
        "/upload",
        files={
            "file": (
                "security_logs.csv",
                csv_content,
                "text/csv"
            )
        }
    )

    assert response.status_code == 200
    assert response.json()["total_events"] == 1


def test_reject_non_csv_file():
    response = client.post(
        "/upload",
        files={
            "file": (
                "notes.txt",
                "hello",
                "text/plain"
            )
        }
    )

    assert response.status_code == 400
