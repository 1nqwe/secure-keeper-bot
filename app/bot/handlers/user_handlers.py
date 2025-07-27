from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.bot.database.database import add_user
from app.bot.keyboards.user_keyboards import to_menu_kb

user_router = Router()

@user_router.message(CommandStart())
async def cmd_start(message: Message):
    await add_user(message.from_user.id, message.from_user.full_name, message.from_user.username)
    await message.answer('Добро пожаловать в SecureKeeper', reply_markup=to_menu_kb())