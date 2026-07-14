from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).parent

load_dotenv(BASE_DIR / ".env")

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID_RAW = os.getenv("ADMIN_ID")
if BOT_TOKEN is None:
    raise ValueError("BOT_TOKEN не найден в .env")
if ADMIN_ID_RAW is None:
    raise ValueError("ADMIN_ID не найден в .env")

ADMIN_ID = int(ADMIN_ID_RAW)

DATABASE_FILE = BASE_DIR / "bot.db"
FILE_NAME = BASE_DIR / "affirmations.json"
APP_NAME = "Affirmation Bot"