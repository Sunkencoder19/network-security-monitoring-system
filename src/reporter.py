def generate_report(analysis, detection):
    print("===== Network Security Monitoring Report =====")
    print("Total Logs:", analysis["total_logs"])
    print("Failed Logins:", analysis["failed_logins"])
    print("Unique IPs:", analysis["unique_ips"])

    print()
    print("===== Security Alerts =====")
    print("Total Alerts:", detection["total_alerts"])
    print("Suspicious IPs:")

    for ip in detection["suspicious_ips"]:
        print(ip)
