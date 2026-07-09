def analyze_logs(logs):
    total_logs = len(logs)

    failed_logins = 0
    for log in logs:
        if log["status"] == "LOGIN_FAILED":
            failed_logins = failed_logins + 1

    unique_ips = set()
    for log in logs:
        unique_ips.add(log["ip"])

    unique_ips = len(unique_ips)

    return {
    "total_logs": total_logs,
    "failed_logins": failed_logins,
    "unique_ips": unique_ips
}
