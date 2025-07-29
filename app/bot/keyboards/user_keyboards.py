from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def to_menu_kb():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Меню", callback_data="to_menu"))
    builder.adjust(1)
    return builder.as_markup()

def main_menu_kb():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Заметки", callback_data="notes_menu"))
    builder.add(InlineKeyboardButton(text="Шифратор", callback_data="encryption_menu"))
    builder.add(InlineKeyboardButton(text="Менеджер паролей", callback_data="password_manager_menu"))
    builder.add(InlineKeyboardButton(text="Генератор", callback_data="generator_menu"))
    builder.add(InlineKeyboardButton(text="Проверка на утечки", callback_data="leaks_menu"))
    builder.adjust(1)
    return builder.as_markup()

def password_manager_menu_kb():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text='Добавить пароль', callback_data='add_password'))
    builder.add(InlineKeyboardButton(text='Мои пароли', callback_data='list_passwords'))
    builder.adjust(1)
    return builder.as_markup()

def my_passwords_kb(passwords):
    builder = InlineKeyboardBuilder()

    for password_id, title, login, password in passwords:
        builder.button(
            text=f"{title}",
            callback_data=f"password_{password_id}"
        )
    builder.button(text="Меню",
                    callback_data="to_menu")
    builder.adjust(1)
    return builder.as_markup()

def password_kb(password_id):
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text='Удалить пароль', callback_data=f'delete_password_{password_id}'))
    builder.add(InlineKeyboardButton(text='Назад', callback_data='list_passwords'))
    builder.adjust(1)
    return builder.as_markup()

def back_to_passwords_list():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text='Назад к списку', callback_data='list_passwords'))
    builder.adjust(1)
    return builder.as_markup()

def generator_menu_kb():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text='Пароль', callback_data='generate_password'))
    builder.add(InlineKeyboardButton(text='Seed-фраза', callback_data='generate_seed_phrase'))
    builder.add(InlineKeyboardButton(text='Назад', callback_data='to_menu'))
    builder.adjust(1)
    return builder.as_markup()

def seed_phrase_kb():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text='Seed-фраза (Русская)', callback_data='russian_seed_phrase'))
    builder.add(InlineKeyboardButton(text='Seed-фраза (Английская)', callback_data='english_seed_phrase'))
    builder.add(InlineKeyboardButton(text='Назад', callback_data='generate_password'))
    builder.adjust(1)
    return builder.as_markup()