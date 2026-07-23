import json
from config import FILE_NAME


def load_affirmations():
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        return json.load(file)


def save_affirmations(items):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(items, file, ensure_ascii=False, indent=4)
