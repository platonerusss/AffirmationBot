import random

def get_random_affirmation(items):
    return random.choice(items)


def add_affirmation(items, text):
    items.append(text)

def get_all_affirmations_text(items):
    return '\n'.join(items)

def create_default_user_settings():
    return {
        "enabled": False,
        "time": "09:00"
    }

def ensure_user_exists(users, user_id):
    if user_id not in users:
        users[user_id] = create_default_user_settings()
