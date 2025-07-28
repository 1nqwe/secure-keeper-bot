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

