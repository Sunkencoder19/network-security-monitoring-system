from parser import parse_log_file
from analyzer import analyze_logs
from detector import detect_suspicious_activity
from reporter import generate_report

file_path = "data/sample_log.txt"

logs = parse_log_file(file_path)

analysis = analyze_logs(logs)

detection = detect_suspicious_activity(logs)

generate_report(analysis, detection)