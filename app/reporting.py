
def generate_report(events, findings):

    severity_levels = {
        "Informational": 0,
        "Low": 1,
        "Medium": 2,
        "High": 3,
        "Critical": 4
    }

    if findings:
        severity = max(
            (f["severity"] for f in findings),
            key=lambda level: severity_levels[level]
        )
    else:
        severity = "Informational"

    if not findings:
        summary = (
            "No suspicious patterns were identified "
            "by the configured detection rules."
        )
    else:
        summary = (
            f"Analysis identified {len(findings)} "
            "potential security findings requiring investigation."
        )

    return {
        "project": "Agentic AI Incident Response Copilot",
        "total_events": len(events),
        "total_findings": len(findings),
        "overall_severity": severity,
        "analyst_summary": summary,
        "findings": findings,
        "recommended_action": (
            "Review the evidence, validate the findings, "
            "and follow your organisation's incident "
            "response procedure."
        ),
        "disclaimer": (
            "Automated analysis is advisory. "
            "Human verification is required."
        )
    }
