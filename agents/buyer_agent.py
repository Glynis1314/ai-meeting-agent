import random

def simulate_responses(users):
    options = ["Morning", "Afternoon", "Evening"]

    responses = {}

    for user in users:
        # Randomly assign availability
        choice = random.choice(options)
        responses[user["email"]] = choice

        print(f"📩 {user['name']} responded: {choice}")

    return responses