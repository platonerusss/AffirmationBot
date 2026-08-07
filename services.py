import random

def get_random_affirmation(items):
    return random.choice(items)


def add_affirmation(items, text):
    items.append(text)

def get_all_affirmations_text(items):
    return '\n'.join(items)
