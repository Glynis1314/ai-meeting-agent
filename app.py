from flask import Flask, render_template
from agents.admin_agent import create_meeting_and_notify
from agents.buyer_agent import simulate_responses
from agents.coordinator_agent import (
    decide_meeting_time,
    send_confirmation,
    send_minutes_of_meeting
)
from data.users import users
import os

app = Flask(__name__)

# 🏠 Home Page (UI)
@app.route("/")
def home():
    return render_template("index.html")


# 📧 Only send emails (optional route)
@app.route("/send-emails")
def send_emails():
    create_meeting_and_notify(users)
    return "Emails Sent Successfully ✅"


# 🤖 FULL SYSTEM (Agentic Flow)
@app.route("/run-system")
def run_system():
    # 1. Admin Agent → send invites
    create_meeting_and_notify(users)

    # 2. Buyer Agents → simulate responses
    responses = simulate_responses(users)

    # 3. Coordinator Agent → decide best time
    best_time = decide_meeting_time(responses)

    # 4. Send confirmation email
    send_confirmation(users, best_time)

    # 5. Send Minutes of Meeting
    send_minutes_of_meeting(users, best_time)

    # 6. Show result on UI
    return render_template("result.html", time=best_time)


# 🚀 Run App (Production Ready)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))