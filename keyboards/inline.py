from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_inline_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Перевести сообщение", callback_data="translate")],
            [InlineKeyboardButton(text="История переводов", callback_data="history")],
            [InlineKeyboardButton(text="Помощь", callback_data="help")],
            [InlineKeyboardButton(text="О боте", callback_data="about")],
            [InlineKeyboardButton(text="Контакты", callback_data="contacts")],
            [InlineKeyboardButton(text="Назад", callback_data="back")]
        ]
    )
    return keyboard