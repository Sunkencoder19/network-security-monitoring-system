def detect_suspicious_activity(logs):
    failed_attempts = {}

    for log in logs:
        if log["status"] == "LOGIN_FAILED":
            if log["ip"] in failed_attempts:
                failed_attempts[log["ip"]] += 1
            else:
                failed_attempts[log["ip"]] = 1

    suspicious_ips = []

    for ip, count in failed_attempts.items():
        if count > 5:
            suspicious_ips.append(ip)

    return {
        "suspicious_ips": suspicious_ips,
        "total_alerts": len(suspicious_ips)
    }