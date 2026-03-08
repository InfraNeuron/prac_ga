import requests
import time
import smtplib
from email.mime.text import MIMEText

# ---------------- CONFIG ----------------
URL_TO_CHECK = "https://example.com"
CHECK_INTERVAL = 20  # half minutes (20 seconds)
MAX_FAILURES = 3

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password"  # Gmail App Password
RECEIVER_EMAIL = "your_email@gmail.com"
# ----------------------------------------

failure_count = 0


def send_email_alert():
    subject = "🚨 URL Down Alert"
    body = f"The URL {URL_TO_CHECK} is not reachable for {MAX_FAILURES} consecutive checks."

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)

    print("Alert email sent.")


def check_url():
    global failure_count
    try:
        response = requests.get(URL_TO_CHECK, timeout=10)
        if 200 <= response.status_code < 300:
            print(f"[SUCCESS] {URL_TO_CHECK} - {response.status_code}")
            failure_count = 0
        else:
            print(f"[FAIL] Status Code: {response.status_code}")
            failure_count += 1
    except requests.RequestException as e:
        print(f"[ERROR] URL not reachable: {e}")
        failure_count += 1

    if failure_count >= MAX_FAILURES:
        send_email_alert()
        failure_count = 0  # reset after alert


if __name__ == "__main__":
    print("Starting URL monitoring...")
    while True:
        check_url()
        time.sleep(CHECK_INTERVAL)