def generate_report(analysis, detection, threat_data):
    print("===== Network Security Monitoring Report =====")
    print("Total Logs:", analysis["total_logs"])
    print("Failed Logins:", analysis["failed_logins"])
    print("Unique IPs:", analysis["unique_ips"])

    print()
    print("===== Security Alerts =====")
    print("Total Alerts:", detection["total_alerts"])

    print()
    print("Brute Force Detected:")

    if detection["suspicious_ips"]:
        for ip in detection["suspicious_ips"]:
            print(ip)
            print("  Abuse Score :", threat_data[ip]["abuse_confidence_score"])
            print("  Country     :", threat_data[ip]["country"])
            print("  ISP         :", threat_data[ip]["isp"])
            print("  Usage Type  :", threat_data[ip]["usage_type"])
            print("  Reports     :", threat_data[ip]["total_reports"])
            print("  Last Report :", threat_data[ip]["last_reported_at"])
            print()
    else:
        print("None")

    print()
    print("Successful Login After Brute Force:")
    if detection["successful_after_bruteforce"]:
        for ip in detection["successful_after_bruteforce"]:
            print(ip)
    else:
        print("None")