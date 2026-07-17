import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

API_KEY = os.getenv("ABUSEIPDB_API_KEY")


def check_ip_reputation(ip):

    fallback_data = {
        "abuse_confidence_score": "N/A",
        "country": "N/A",
        "isp": "N/A",
        "usage_type": "N/A",
        "total_reports": "N/A",
        "last_reported_at": "N/A"
    }

    if not API_KEY:
        print("⚠ AbuseIPDB API key not found. Skipping threat intelligence lookup.")
        return fallback_data

    url = "https://api.abuseipdb.com/api/v2/check"

    headers = {
        "Key": API_KEY,
        "Accept": "application/json"
    }

    params = {
        "ipAddress": ip
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            timeout=10
        )

        response.raise_for_status()

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

    except requests.exceptions.RequestException as e:
        print(f"⚠ Threat Intelligence lookup failed: {e}")
        return fallback_data

    except (KeyError, ValueError) as e:
        print(f"⚠ Invalid response received from AbuseIPDB: {e}")
        return fallback_data