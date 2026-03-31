from flask import Flask
from agents.admin_agent import create_meeting_and_notify
from agents.buyer_agent import simulate_responses
from agents.coordinator_agent import decide_meeting_time, send_confirmation, send_minutes_of_meeting
from data.users import users
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# Step 2: Only send emails (you already have this)
@app.route("/send-emails")
def send_emails():
    create_meeting_and_notify(users)
    return "Emails Sent Successfully ✅"

# 🔥 Step 3: FULL SYSTEM (Agentic flow)
@app.route("/run-system")
def run_system():
    create_meeting_and_notify(users)
    responses = simulate_responses(users)
    best_time = decide_meeting_time(responses)

    send_confirmation(users, best_time)
    send_minutes_of_meeting(users, best_time)

    return f"Meeting scheduled and MOM sent at: {best_time} ✅"


if __name__ == "__main__":
    app.run(debug=True)