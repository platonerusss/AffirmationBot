from pathlib import Path
import os

from dotenv import load_dotenv


BASE_DIR = Path(__file__).parent

load_dotenv(BASE_DIR / ".env")


BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID_RAW = os.getenv("ADMIN_ID")

if BOT_TOKEN is None:
    raise ValueError("BOT_TOKEN не найден в .env")

if ADMIN_ID_RAW is None:
    raise ValueError("ADMIN_ID не найден в .env")

ADMIN_ID = int(ADMIN_ID_RAW)


DATA_DIR = Path(
    os.getenv("DATA_DIR")
    or os.getenv("RAILWAY_VOLUME_MOUNT_PATH")
    or BASE_DIR
)

DATA_DIR.mkdir(parents=True, exist_ok=True)


AFFIRMATIONS_FILE = DATA_DIR / "affirmations.json"
DATABASE_FILE = DATA_DIR / "bot.db"

# Оставляем для совместимости, если где-то старый код ещё использует FILE_NAME
FILE_NAME = AFFIRMATIONS_FILE

APP_NAME = "Affirmation Bot"