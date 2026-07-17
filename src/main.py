from parser import parse_log_file
from analyzer import analyze_logs
from detector import detect_suspicious_activity
import json
from threat_intelligence import check_ip_reputation
from report_generator import generate_html_report

file_path = "data/sample_log.txt"

logs = parse_log_file(file_path)

analysis = analyze_logs(logs)

try:
    with open("config.json", "r") as file:
        config = json.load(file)

except FileNotFoundError:
    print("❌ Error: 'config.json' not found.")
    raise SystemExit(1)

except json.JSONDecodeError:
    print("❌ Error: 'config.json' contains invalid JSON.")
    raise SystemExit(1)

except Exception as e:
    print(f"❌ Unexpected error while loading configuration: {e}")
    raise SystemExit(1)

detection = detect_suspicious_activity(logs, config)

threat_data = {}

for ip in detection["suspicious_ips"]:
    threat_data[ip] = check_ip_reputation(ip)


generate_html_report(
    analysis,
    detection,
    threat_data
)

print("\n==================================================")
print("      Network Security Monitoring System")
print("==================================================\n")

print("Analysis completed successfully.\n")

print("Report generated:")
print("→ reports/security_report.html")
print("")