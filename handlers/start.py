from aiogram import types
from aiogram.filters.command import Command
from keyboards.inline import get_inline_keyboard


async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! Я бот для преобразования текста в голос!",
        reply_markup=get_inline_keyboard()
    )


def register_handlers(dp):
    dp.message.register(cmd_start, Command("start"))