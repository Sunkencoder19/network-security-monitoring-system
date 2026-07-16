import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

API_KEY = os.getenv("ABUSEIPDB_API_KEY")

def check_ip_reputation(ip):
    url = "https://api.abuseipdb.com/api/v2/check"

    headers = {
    "Key": API_KEY,
    "Accept": "application/json"
}

    params = {
    "ipAddress": ip
}
    
    response = requests.get(
    url,
    headers=headers,
    params=params,
    timeout=10
)
    if response.status_code != 200:
        return {
        "abuse_confidence_score": "N/A",
        "country": "N/A",
        "isp": "N/A",
        "usage_type": "N/A",
        "total_reports": "N/A",
        "last_reported_at": "N/A"
    }

    data = response.json()

    last_report = data["data"]["lastReportedAt"]
    
    if last_report:
        last_report = datetime.fromisoformat(last_report)
        last_report = last_report.strftime("%d %b %Y, %H:%M UTC")
    else:
        last_report = "Never"

    return {
    "abuse_confidence_score": data["data"]["abuseConfidenceScore"],
    "country": data["data"]["countryCode"],
    "isp": data["data"]["isp"],
    "usage_type": data["data"]["usageType"],
    "total_reports": data["data"]["totalReports"],
    "last_reported_at": last_report
}