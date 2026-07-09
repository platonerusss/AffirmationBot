from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from services import ensure_user_exists

from storage import load_users, save_users

router = Router()

@router.message(Command("settings"))
async def settings_handler(message: Message):
    users = load_users()
    user_id = str(message.from_user.id)
    ensure_user_exists(users, user_id)
    save_users(users)

    settings = users[user_id]
    status = "включена" if settings["enabled"] else "выключена"
    await message.answer(f"""Твои настройки:
Ежедневная аффирмация: {status}
Время: {settings["time"]}""")



@router.message(Command("on"))
async def on_handler(message: Message):
    users = load_users()
    user_id = str(message.from_user.id)
    ensure_user_exists(users, user_id)
    users[user_id]["enabled"] = True
    save_users(users)
    await message.answer("Ежедневная аффирмация включена")


@router.message(Command("off"))
async def off_handler(message: Message):
    users = load_users()
    user_id = str(message.from_user.id)
    ensure_user_exists(users, user_id)
    users[user_id]["enabled"] = False
    save_users(users)
    await message.answer("Ежедневная аффирмация выключена")
