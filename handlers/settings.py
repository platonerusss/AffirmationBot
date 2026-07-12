from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from database import get_user_settings, set_user_enabled, set_user_time

router = Router()

@router.message(Command("settings"))
async def settings_handler(message: Message):
    user_id = message.from_user.id
    settings = get_user_settings(user_id)
    status = "включена" if settings["enabled"] else "выключена"
    await message.answer(f"""Твои настройки:
Ежедневная аффирмация: {status}
Время: {settings["time"]}""")


@router.message(Command("on"))
async def on_handler(message: Message):
    user_id = message.from_user.id
    set_user_enabled(user_id, True)
    await message.answer("Ежедневная аффирмация включена")


@router.message(Command("off"))
async def off_handler(message: Message):
    user_id = message.from_user.id
    set_user_enabled(user_id, False)
    await message.answer("Ежедневная аффирмация выключена")


@router.message(Command("settime"))
async def settime_handler(message: Message):
    user_id = message.from_user.id
    new_time = message.text.replace("/settime", "", 1).strip()
    if len(new_time) != 5 or new_time[2] != ":":
        await message.answer("Неверное время. Напиши время так: /settime 09:00")
        return
    hours = new_time[:2]
    minutes = new_time[3:]
    if not hours.isdigit() or not minutes.isdigit():
        await message.answer("Неверное время. Напиши время так: /settime 09:00")
        return
    hours_number = int(hours)
    minutes_number = int(minutes)
    if not (0 <= hours_number <= 23 and 0 <= minutes_number <= 59):
        await message.answer("Неверное время. Напиши время так: /settime 09:00")
        return
    set_user_time(user_id, new_time)
    await message.answer(f"Время ежедневной аффирмации изменено на {new_time}")

    
