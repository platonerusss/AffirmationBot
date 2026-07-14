import asyncio
from datetime import datetime

from database import get_all_users
from storage import load_affirmations
from services import get_random_affirmation

async def check_daily_affirmations(bot):
    while True:
        current_time = datetime.now().strftime("%H:%M")
        rows = get_all_users()
        for user_id, enabled, user_time in rows:
            if enabled and user_time == current_time:
                items = load_affirmations()
                text = get_random_affirmation(items)
                await bot.send_message(user_id, text)
        await asyncio.sleep(60)
