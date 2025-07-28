import asyncio

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from app.bot.database.database import add_user, add_password
from app.bot.keyboards.user_keyboards import to_menu_kb, main_menu_kb, password_manager_menu_kb
from app.bot.states.user_states import AddPassword

user_router = Router()

@user_router.message(CommandStart())
async def cmd_start(message: Message):
    await add_user(message.from_user.id, message.from_user.full_name, message.from_user.username)
    await message.answer('Добро пожаловать в SecureKeeper', reply_markup=to_menu_kb())

@user_router.callback_query(F.data == 'to_menu')
async def main_menu(call: CallbackQuery):
    await call.message.edit_text('Меню', reply_markup=main_menu_kb())

@user_router.callback_query(F.data == 'password_manager_menu')
async def password_manager_menu(call: CallbackQuery):
    await call.message.edit_text('Выберите действие', reply_markup=password_manager_menu_kb())

@user_router.callback_query(F.data == 'add_password')
async def add_password_step_1(call: CallbackQuery, state: FSMContext):
    await state.set_state(AddPassword.title)
    await call.message.edit_text('Введите заголовок:\n\n'
                                 '<i>это сообщение удалится через 5 секунд</i>',reply_markup=to_menu_kb(), parse_mode="HTML")
    await asyncio.sleep(5)
    await call.message.delete()


@user_router.message(AddPassword.title)
async def add_password_step_2(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    await state.set_state(AddPassword.login)
    msg = await message.answer('Введите логин:\n\n'
                        '<i>это сообщение удалится через 5 секунд</i>', parse_mode="HTML")
    await asyncio.sleep(5)
    await msg.delete()
    await message.delete()

@user_router.message(AddPassword.login)
async def add_password_step_3(message: Message, state: FSMContext):
    await state.update_data(login=message.text)
    await state.set_state(AddPassword.password)
    msg = await message.answer('Введите Пароль:\n\n'
                         '<i>это сообщение удалится через 5 секунд</i>', parse_mode="HTML")
    await asyncio.sleep(5)
    await msg.delete()
    await message.delete()

@user_router.message(AddPassword.password)
async def add_password_step_4(message: Message, state: FSMContext):
    await state.update_data(password=message.text)
    data = await state.get_data()
    try:
        await add_password(
            user_id=message.from_user.id,
            title=data['title'],
            login=data['login'],
            password=data['password']
        )
    except:
        await message.delete()

        await message.answer('Произошла ошибка при сохранении пароля', reply_markup=to_menu_kb())
    else:
        await message.delete()
        await message.answer('Данные успешно добавлены', reply_markup=to_menu_kb())
    finally:
        await state.clear()

