
def detect_threats(events):

    findings = []
    failed_logins = {}

    for event in events:

        event_type = event.get("event_type", "").lower()
        ip = event.get("source_ip", "Unknown")
        details = event.get("details", "").lower()

        # Detect repeated failed logins
        if event_type == "login_failed":
            failed_logins[ip] = failed_logins.get(ip, 0) + 1

        # Detect suspicious PowerShell commands
        if "powershell" in event_type:
            if any(term in details for term in [
                "encodedcommand",
                "-enc",
                "downloadstring"
            ]):
                findings.append({
                    "threat": "Suspicious PowerShell Execution",
                    "severity": "High",
                    "source_ip": ip,
                    "evidence": details
                })

        # Detect privilege escalation
        if "privilege_escalation" in event_type:
            findings.append({
                "threat": "Possible Privilege Escalation",
                "severity": "Critical",
                "source_ip": ip,
                "evidence": details
            })

        # Detect unusually large outbound transfers
        try:
            bytes_out = int(event.get("bytes_out", 0))
        except (ValueError, TypeError):
            bytes_out = 0

        if bytes_out >= 50 * 1024 * 1024:
            findings.append({
                "threat": "Large Outbound Data Transfer",
                "severity": "Medium",
                "source_ip": ip,
                "evidence": f"{bytes_out} bytes transferred"
            })

    # Identify possible brute-force attacks
    for ip, count in failed_logins.items():

        if count >= 5:
            findings.append({
                "threat": "Possible Brute Force Attack",
                "severity": "High",
                "source_ip": ip,
                "evidence": f"{count} failed login attempts"
            })

    return findings
