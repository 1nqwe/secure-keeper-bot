from aiogram.fsm.state import StatesGroup, State


class AddPassword(StatesGroup):
    title = State()
    login = State()
    password = State()

class AddNote(StatesGroup):
    title = State()
    note = State()