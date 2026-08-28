import json
import shutil

from config import AFFIRMATIONS_FILE, BASE_DIR


SOURCE_AFFIRMATIONS_FILE = BASE_DIR / "affirmations.json"

DEFAULT_AFFIRMATIONS = {
    "female": [],
    "male": []
}


def has_affirmations(data):
    return bool(data.get("female")) or bool(data.get("male"))


def read_json_file(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def ensure_affirmations_file():
    if not AFFIRMATIONS_FILE.exists():
        if SOURCE_AFFIRMATIONS_FILE.exists() and SOURCE_AFFIRMATIONS_FILE != AFFIRMATIONS_FILE:
            shutil.copy(SOURCE_AFFIRMATIONS_FILE, AFFIRMATIONS_FILE)
            return

        save_affirmations(DEFAULT_AFFIRMATIONS)
        return

    data = read_json_file(AFFIRMATIONS_FILE)

    if has_affirmations(data):
        return

    if SOURCE_AFFIRMATIONS_FILE.exists() and SOURCE_AFFIRMATIONS_FILE != AFFIRMATIONS_FILE:
        source_data = read_json_file(SOURCE_AFFIRMATIONS_FILE)

        if has_affirmations(source_data):
            save_affirmations(source_data)
            return

    save_affirmations(DEFAULT_AFFIRMATIONS)


def load_affirmations():
    ensure_affirmations_file()

    return read_json_file(AFFIRMATIONS_FILE)


def save_affirmations(items):
    with open(AFFIRMATIONS_FILE, "w", encoding="utf-8") as file:
        json.dump(items, file, ensure_ascii=False, indent=4)
