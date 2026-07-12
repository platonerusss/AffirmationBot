from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).parent

load_dotenv(BASE_DIR / ".env")

BOT_TOKEN = os.getenv("BOT_TOKEN")

if BOT_TOKEN is None:
    raise ValueError("BOT_TOKEN не найден в .env")

DATABASE_FILE = BASE_DIR / "bot.db"
FILE_NAME = BASE_DIR / "affirmations.json"
USERS_FILE = BASE_DIR / "users.json"
APP_NAME = "Affirmation Bot"