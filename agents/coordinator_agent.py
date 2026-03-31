from collections import Counter
from services.email_service import send_email

# 🔹 Decision Logic
def decide_meeting_time(responses):
    counts = Counter(responses.values())
    best_time = counts.most_common(1)[0][0]

    print("\n📊 Availability Summary:", counts)
    print("✅ Final Meeting Time:", best_time)

    return best_time


# 🔹 Send Confirmation Email
def send_confirmation(users, best_time):
    subject = "Meeting Confirmed ✅"

    for user in users:
        body = f"""
Hi {user['name']},

The meeting has been scheduled successfully.

🕒 Time: {best_time}

Thanks,
AI Meeting Coordinator
        """

        send_email(user["email"], subject, body)


# 🔹 Send Minutes of Meeting
def send_minutes_of_meeting(users, best_time):
    subject = "Minutes of Meeting 📄"

    summary = f"""
Meeting Summary:

- Meeting Time: {best_time}
- Discussion: Product features and improvements
- Key Points:
    • Feature A needs improvement
    • Marketing strategy discussed
    • Timeline finalized
"""

    for user in users:
        body = f"""
Hi {user['name']},

Here are the Minutes of the Meeting:

{summary}

Best,
AI Meeting Coordinator
        """

        send_email(user["email"], subject, body)