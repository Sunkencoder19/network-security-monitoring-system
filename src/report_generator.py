from datetime import datetime


def generate_html_report(analysis, detection, threat_data):

    # Read HTML template
    with open("templates/report_template.html", "r", encoding="utf-8") as file:
        html = file.read()
    

    # Generate timestamp
    generated_time = datetime.now().strftime("%d %B %Y %I:%M %p")
    report_id = datetime.now().strftime("NSM-%Y%m%d-%H%M%S")

    # Risk banner
    if detection["total_alerts"] == 0:
        risk_banner = "🟢 LOW RISK • No suspicious activity detected."
    else:
        alerts = detection["total_alerts"]

        if alerts == 1:
            risk_banner = (
                f"🔴 HIGH RISK • {alerts} suspicious activity detected."
        )
        else:
            risk_banner = (
                f"🔴 HIGH RISK • {alerts} suspicious activities detected."
        )

    # Summary cards
    summary_cards = f"""
    <div class="card blue">
        <h3>📄 Total Logs</h3>
        <p>{analysis["total_logs"]}</p>
    </div>

    <div class="card red">
        <h3>❌ Failed Logins</h3>
        <p>{analysis["failed_logins"]}</p>
    </div>

    <div class="card green">
        <h3>🌐 Unique IPs</h3>
        <p>{analysis["unique_ips"]}</p>
    </div>

    <div class="card orange">
        <h3>🚨 Alerts</h3>
        <p>{detection["total_alerts"]}</p>
    </div>
    """

    summary_text = (
    f"This report analyzed <strong>{analysis['total_logs']}</strong> "
    f"authentication events from "
    f"<strong>{analysis['unique_ips']}</strong> unique IP addresses. "
    f"A total of <strong>{detection['total_alerts']}</strong> suspicious "
    f"{'activity was' if detection['total_alerts'] == 1 else 'activities were'} "
    f"detected during the analysis."
)

    # Threat Intelligence Table
    if not threat_data:

        threat_table = """
        <p>No suspicious IPs were detected.</p>
        """

    else:

        threat_table = """
        <table>
            <thead>
                <tr>
                    <th>IP Address</th>
                    <th>Abuse Score</th>
                    <th>Country</th>
                    <th>ISP</th>
                    <th>Usage Type</th>
                    <th>Total Reports</th>
                    <th>Last Report</th>
                </tr>
            </thead>
            <tbody>
        """

        for ip, data in threat_data.items():
            score = data["abuse_confidence_score"]

            if score <= 20:
                score_class = "score-low"
            elif score <= 60:
                score_class = "score-medium"
            else:
                score_class = "score-high"

            threat_table += f"""
                <tr>
                    <td>{ip}</td>
                    <td class="{score_class}">{score}</td>
                    <td>{data["country"]}</td>
                    <td>{data["isp"]}</td>
                    <td>{data["usage_type"]}</td>
                    <td>{data["total_reports"]}</td>
                    <td>{data["last_reported_at"]}</td>
                </tr>
            """

        threat_table += """
            </tbody>
        </table>
        """

    # Placeholder for next section
    # Successful Login After Brute Force Table

    successful_logins = detection["successful_after_bruteforce"]

    if not successful_logins:

        successful_login_table = """
        <p>No successful login after brute force detected.</p>
        """

    else:

        successful_login_table = """
        <table>
            <thead>
                <tr>
                    <th>IP Address</th>
                </tr>
            </thead>
            <tbody>
        """

        for ip in successful_logins:

            successful_login_table += f"""
                <tr>
                    <td>{ip}</td>
                </tr>
            """

        successful_login_table += """
            </tbody>
        </table>
        """

    # Replace placeholders
    html = html.replace("{{generated_time}}", generated_time)
    html = html.replace("{{risk_banner}}", risk_banner)
    html = html.replace("{{summary_cards}}", summary_cards)
    html = html.replace("{{threat_table}}", threat_table)
    html = html.replace("{{successful_login_table}}", successful_login_table)
    html = html.replace("{{summary_text}}", summary_text)
    html = html.replace("{{report_id}}", report_id)

    # Save report
    with open(
        "reports/security_report.html",
        "w",
        encoding="utf-8"
    ) as file:
        file.write(html)

    print("HTML report generated successfully!")