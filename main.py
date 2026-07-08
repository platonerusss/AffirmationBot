import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN

from handlers.start import router as start_router
from handlers.common import router as common_router
from handlers.affirmations import router as affirmation_router
from handlers.help import router as help_router


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp.include_router(start_router)
dp.include_router(affirmation_router)
dp.include_router(help_router)
dp.include_router(common_router)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())