def generate_report(analysis, detection):
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
    else:
        print("None")

    print()
    print("Successful Login After Brute Force:")
    if detection["successful_after_bruteforce"]:
        for ip in detection["successful_after_bruteforce"]:
            print(ip)
    else:
        print("None")