from services.email_service import send_email

def create_meeting_and_notify(users):
    subject = "Meeting Invitation: Product Discussion"

    for user in users:
        body = f"""
Hi {user['name']},

You are invited to a product discussion meeting.

Please reply with your availability:
- Morning
- Afternoon
- Evening

(This is a test for an academic project)

Thanks,
Admin
        """

        send_email(user["email"], subject, body)