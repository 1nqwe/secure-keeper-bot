import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from app.bot.handlers.user_handlers import user_router



async def startup():
    print('Bot is starting...')

async def shutdown():
    print('Bot is shutting down...')


async def main():
    load_dotenv()
    bot = Bot(token = os.getenv("BOT_TOKEN"))
    dp = Dispatcher()
    dp.include_router(user_router)
    dp.startup.register(startup)
    dp.shutdown.register(shutdown)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass