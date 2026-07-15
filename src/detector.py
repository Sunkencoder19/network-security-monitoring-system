def detect_suspicious_activity(logs, config):
    failed_attempts = {}

    for log in logs:
        if log["status"] == "LOGIN_FAILED":
            if log["ip"] in failed_attempts:
                failed_attempts[log["ip"]] += 1
            else:
                failed_attempts[log["ip"]] = 1

    suspicious_ips = set()

    for ip, count in failed_attempts.items():
        if count > config["failed_login_threshold"]:
            suspicious_ips.add(ip)

    successful_after_bruteforce = set()

    for log in logs:
        if log["status"] == "LOGIN_SUCCESS":
            if log["ip"] in suspicious_ips:
                successful_after_bruteforce.add(log["ip"])

    
    return {
    "suspicious_ips": suspicious_ips,
    "successful_after_bruteforce": successful_after_bruteforce,
    "total_alerts": len(suspicious_ips) + len(successful_after_bruteforce)
}