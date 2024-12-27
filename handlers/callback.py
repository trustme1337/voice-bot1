from aiogram import types
from utils.history import get_history


async def handle_callback(callback: types.CallbackQuery):
    if callback.data == "translate":
        await callback.message.answer("Отправьте текст, чтобы преобразовать его в голос.")
    elif callback.data == "history":
        user_id = callback.from_user.id
        user_history = get_history(user_id)
        if user_history:
            history_text = "\n".join(user_history)
            await callback.message.answer(f"История переводов:\n{history_text}")
        else:
            await callback.message.answer("История переводов пуста.")
    elif callback.data == "help":
        await callback.message.answer("Этот бот преобразует текстовые сообщения в голосовые. Просто отправьте текст!")
    elif callback.data == "about":
        await callback.message.answer("Это бот для преобразования текста в голос. Автор: Владислав Музалевский")
    elif callback.data == "contacts":
        await callback.message.answer("Контакты: trustme777@gmail.com.")
    elif callback.data == "back":
        await callback.message.delete()
        from keyboards.inline import get_inline_keyboard
        await callback.message.answer("Возвращаемся назад!", reply_markup=get_inline_keyboard())


def register_handlers(dp):
    dp.callback_query.register(handle_callback)