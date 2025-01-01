# chatbot.py

def handle_user_query(user_message):
    """
    Process the user message and categorize the query.
    :param user_message: str, user message
    :return: tuple (bot_reply: str, category: str)
    """
    categories = {
        "1": "Music",
        "2": "Sports",
        "3": "Education",
        "4": "Technology",
        "5": "Health"
    }

    response_template = """
    Here are the event categories:
    1. Music
    2. Sports
    3. Education
    4. Technology
    5. Health
    Enter the number of the event you're interested in:
    """
    
    if user_message.isdigit() and user_message in categories:
        category = categories[user_message]
        bot_reply = f"Great! You've selected {category}. We'll show you more about {category} events!"
        return bot_reply, category
    else:
        return response_template.strip(), None
