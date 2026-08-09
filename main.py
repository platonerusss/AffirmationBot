import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN

from handlers.start import router as start_router
from handlers.common import router as common_router
from handlers.affirmations import router as affirmation_router
from handlers.help import router as help_router
from handlers.settings import router as settings_router
from handlers.debug import router as debug_router
from database import init_db
from scheduler import check_daily_affirmations

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp.include_router(start_router)
dp.include_router(affirmation_router)
dp.include_router(help_router)
dp.include_router(settings_router)
dp.include_router(debug_router)
dp.include_router(common_router)


async def main():
    init_db()
    asyncio.create_task(check_daily_affirmations(bot))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

    