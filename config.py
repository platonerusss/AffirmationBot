from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).parent

load_dotenv(BASE_DIR / ".env")

BOT_TOKEN = os.getenv("BOT_TOKEN")

if BOT_TOKEN is None:
    raise ValueError("BOT_TOKEN не найден в .env")

FILE_NAME = BASE_DIR / "affirmations.json"
APP_NAME = "Affirmation Bot"