from parser import parse_log_file
from analyzer import analyze_logs
from detector import detect_suspicious_activity
from reporter import generate_report
import json
from threat_intelligence import check_ip_reputation

file_path = "data/sample_log.txt"

logs = parse_log_file(file_path)

analysis = analyze_logs(logs)

with open("config.json", "r") as file:
    config = json.load(file)

detection = detect_suspicious_activity(logs, config)

threat_data = {}

for ip in detection["suspicious_ips"]:
    threat_data[ip] = check_ip_reputation(ip)

generate_report(
    analysis,
    detection,
    threat_data
)