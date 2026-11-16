from app.detection import detect_threats


def test_detect_brute_force_attack():
    events = [
        {
            "event_type": "login_failed",
            "source_ip": "203.0.113.25",
            "details": "Invalid password"
        }
        for _ in range(5)
    ]

    findings = detect_threats(events)

    assert any(
        finding["threat"] == "Possible Brute Force Attack"
        for finding in findings
    )


def test_detect_privilege_escalation():
    events = [{
        "event_type": "privilege_escalation",
        "source_ip": "198.51.100.10",
        "details": "Unexpected admin privilege"
    }]

    findings = detect_threats(events)

    assert any(
        finding["threat"] == "Possible Privilege Escalation"
        for finding in findings
    )
