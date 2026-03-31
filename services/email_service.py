import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

def send_email(to_email, subject, body):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL, PASSWORD)

        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(EMAIL, to_email, message)
        server.quit()

        print(f"✅ Email sent to {to_email}")

    except Exception as e:
        print(f"❌ Failed to send email to {to_email}: {e}")