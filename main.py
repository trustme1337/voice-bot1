from aiogram import Bot, Dispatcher
from handlers import start, text, callback
from config import TOKEN
import asyncio

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    start.register_handlers(dp)
    text.register_handlers(dp)
    callback.register_handlers(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())