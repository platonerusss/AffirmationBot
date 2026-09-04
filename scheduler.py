import asyncio
import logging
from datetime import datetime, timezone, timedelta

from aiogram.exceptions import TelegramAPIError

from database import get_all_users, set_user_last_sent_date
from storage import load_affirmations
from services import get_random_affirmation


LOCAL_TZ = timezone(timedelta(hours=3))
logger = logging.getLogger(__name__)


async def check_daily_affirmations(bot):
    while True:
        now = datetime.now(LOCAL_TZ)
        current_time = now.strftime("%H:%M")
        current_date = now.strftime("%Y-%m-%d")

        rows = get_all_users()

        for user_id, enabled, user_time, last_sent_date, mode in rows:
            if enabled and user_time <= current_time and last_sent_date != current_date:
                data = load_affirmations()
                text = get_random_affirmation(data, mode)

                try:
                    await bot.send_message(user_id, text)
                except TelegramAPIError:
                    logger.exception(
                        "Не удалось отправить ежедневную аффирмацию пользователю %s",
                        user_id,
                    )
                    continue

                set_user_last_sent_date(user_id, current_date)

        await asyncio.sleep(60)
