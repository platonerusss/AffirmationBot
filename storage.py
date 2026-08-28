import json

from config import AFFIRMATIONS_FILE


DEFAULT_AFFIRMATIONS = {
    "female": [],
    "male": []
}


def load_affirmations():
    if not AFFIRMATIONS_FILE.exists():
        save_affirmations(DEFAULT_AFFIRMATIONS)

    with open(AFFIRMATIONS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_affirmations(items):
    with open(AFFIRMATIONS_FILE, "w", encoding="utf-8") as file:
        json.dump(items, file, ensure_ascii=False, indent=4)
