from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

button_affirmation = KeyboardButton(text="Получить аффирмацию")
button_all = KeyboardButton(text="Все аффирмации")
button_help = KeyboardButton(text="Помощь")


main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [button_affirmation],
        [button_all, button_help]
    ],
    resize_keyboard=True
)

again_affirmation_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Еще одну",
                callback_data="new_affirmation"
            )
        ]
    ]
)