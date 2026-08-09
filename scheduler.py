import asyncio
from datetime import datetime, timezone, timedelta

from database import get_all_users, set_user_last_sent_date
from storage import load_affirmations
from services import get_random_affirmation

LOCAL_TZ = timezone(timedelta(hours=3))

async def check_daily_affirmations(bot):
    while True:
        now = datetime.now(LOCAL_TZ)
        current_time = now.strftime("%H:%M")
        current_date = now.strftime("%Y-%m-%d")
        rows = get_all_users()
        for user_id, enabled, user_time, last_sent_date in rows:
            if enabled and user_time == current_time and current_date != last_sent_date:
                set_user_last_sent_date(user_id, current_date)
                items = load_affirmations()
                text = get_random_affirmation(items)
                await bot.send_message(user_id, text)
        await asyncio.sleep(60)
