from app.reporting import generate_report


def test_report_with_no_findings():
    report = generate_report([], [])

    assert report["total_events"] == 0
    assert report["total_findings"] == 0
    assert report["overall_severity"] == "Informational"


def test_report_with_critical_finding():
    events = [{"event_type": "privilege_escalation"}]

    findings = [{
        "threat": "Possible Privilege Escalation",
        "severity": "Critical",
        "source_ip": "198.51.100.10",
        "evidence": "Unexpected admin privilege"
    }]

    report = generate_report(events, findings)

    assert report["total_findings"] == 1
    assert report["overall_severity"] == "Critical"
