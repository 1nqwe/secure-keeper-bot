import asyncio

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from app.bot.database.database import add_user, add_password, get_all_user_passwords, get_password_info, delete_password
from app.bot.keyboards.user_keyboards import to_menu_kb, main_menu_kb, password_manager_menu_kb, my_passwords_kb, \
    password_kb, back_to_passwords_list, generator_menu_kb, seed_phrase_kb
from app.bot.states.user_states import AddPassword
from app.security.password import generate_password
from app.security.seed_phrase import generate_seed_phrase

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

@user_router.callback_query(F.data == 'list_passwords')
async def list_passwords(call: CallbackQuery):
    passwords = await get_all_user_passwords(call.from_user.id)
    await call.message.edit_text('Список', reply_markup=my_passwords_kb(passwords))

@user_router.callback_query(F.data.startswith("password_"))
async def task_info(call: CallbackQuery):
    password_id = call.data.split("_")[1]
    password_info = await get_password_info(password_id)
    title, login, password, created_at = password_info
    message = (
                f"<b>Название:</b> <code>{title}</code>\n"
                f"<b>Логин:</b> <code>{login}</code>\n"
                f"<b>Пароль:</b> <code>{password}</code>\n"
                f"<b>Дата создания:</b> <code>{created_at.split()[0]}</code>"
    )
    await call.message.edit_text(message, reply_markup=password_kb(password_id), parse_mode="HTML")

@user_router.callback_query(F.data.startswith("delete_password_"))
async def del_task(call: CallbackQuery):
    password_id = call.data.split("_")[2]
    await delete_password(password_id)
    await call.message.edit_text('Пароль удален', reply_markup=back_to_passwords_list())


@user_router.callback_query(F.data == 'generator_menu')
async def generator_menu(call: CallbackQuery):
    await call.message.edit_text('Выберите что сгенерировать', reply_markup=generator_menu_kb())

@user_router.callback_query(F.data == 'generate_password')
async def generate_password_hand(call: CallbackQuery):
    await call.message.edit_text(f'Ваш сгенерированный пароль:\n'
                                 f'<code>{generate_password()}</code>',
                                 reply_markup=to_menu_kb(), parse_mode='HTML')

@user_router.callback_query(F.data == 'generate_seed_phrase')
async def generate_seed_phrase_language(call: CallbackQuery):
    await call.message.edit_text('Выберите язык генерации:', reply_markup=seed_phrase_kb())

@user_router.callback_query(F.data == 'russian_seed_phrase')
async def russian_phrase(call: CallbackQuery):
    await call.message.edit_text(f'Ваша seed-фраза:\n'
                                 f'<code>{generate_seed_phrase(12, 'russian')}</code>',
                                 reply_markup=to_menu_kb(), parse_mode='HTML')

@user_router.callback_query(F.data == 'english_seed_phrase')
async def english_phrase(call: CallbackQuery):
    await call.message.edit_text(f'Ваша seed-фраза:\n'
                                 f'<code>{generate_seed_phrase(12, 'english')}</code>',
                                 reply_markup=to_menu_kb(), parse_mode='HTML')