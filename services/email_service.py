import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

def send_email(to_email, subject, body):
    try:
        print(f"Sending to {to_email}...")

        # Create message
        msg = MIMEMultipart()
        msg["From"] = EMAIL
        msg["To"] = to_email
        msg["Subject"] = subject

        # Attach body with UTF-8 encoding
        msg.attach(MIMEText(body, "plain", "utf-8"))

        # Send email
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL, PASSWORD)

        server.sendmail(EMAIL, to_email, msg.as_string())
        server.quit()

        print(f"✅ Email sent to {to_email}")

    except Exception as e:
        print(f"❌ Failed to send email to {to_email}: {e}")