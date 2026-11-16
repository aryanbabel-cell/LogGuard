
from flask import Flask, render_template, send_file
import pandas as pd
from pathlib import Path

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent

LOG_FILE = BASE_DIR / "data" / "login_logs.txt"
REPORT_FILE = BASE_DIR / "output" / "security_report.csv"


@app.route("/")
def home():

    # Load data
    logs = pd.read_csv(LOG_FILE)
    df = pd.read_csv(REPORT_FILE)

    # IP statistics
    total_ips = logs["ip_address"].nunique()

    high_risk = (df["risk_level"] == "HIGH").sum()
    medium_risk = (df["risk_level"] == "MEDIUM").sum()
    low_risk = (df["risk_level"] == "LOW").sum()

    # Login statistics
    total_attempts = len(logs)

    successful_attempts = (logs["status"] == "SUCCESS").sum()
    failed_attempts = (logs["status"] == "FAILED").sum()

    # Calculate chart percentages
    success_percent = (
        successful_attempts / total_attempts * 100
        if total_attempts else 0
    )

    failed_percent = (
        failed_attempts / total_attempts * 100
        if total_attempts else 0
    )

    # IP-wise login activity
    ip_activity = (
        logs.groupby(["ip_address", "status"])
        .size()
        .unstack(fill_value=0)
        .reset_index()
    )

    if "SUCCESS" not in ip_activity.columns:
        ip_activity["SUCCESS"] = 0

    if "FAILED" not in ip_activity.columns:
        ip_activity["FAILED"] = 0

    ip_activity = ip_activity.rename(columns={
        "SUCCESS": "successful_logins",
        "FAILED": "failed_logins"
    })

    # Convert data into dictionaries
    reports = df.to_dict(orient="records")
    activity = ip_activity.to_dict(orient="records")

    return render_template(
        "index.html",
        reports=reports,
        activity=activity,
        total_ips=total_ips,
        high_risk=high_risk,
        medium_risk=medium_risk,
        low_risk=low_risk,
        total_attempts=total_attempts,
        successful_attempts=successful_attempts,
        failed_attempts=failed_attempts,
        success_percent=success_percent,
        failed_percent=failed_percent
    )


# Download security report
@app.route("/download")
def download_report():

    return send_file(
        REPORT_FILE,
        as_attachment=True,
        download_name="LogGuard_Security_Report.csv"
    )


if __name__ == "__main__":
    app.run(debug=True)
