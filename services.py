import random


def get_random_affirmation(data, mode):
    items = data[mode]
    return random.choice(items)


def add_affirmation(data, mode, text):
    data[mode].append(text)


def get_all_affirmations_text(data, mode):
    return "\n".join(data[mode])