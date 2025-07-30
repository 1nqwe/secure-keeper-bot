from aiogram.fsm.state import StatesGroup, State


class AddPassword(StatesGroup):
    title = State()
    login = State()
    password = State()

class AddNote(StatesGroup):
    title = State()
    note = State()

class Encoder(StatesGroup):
    encode_base64 = State()
    encode_base32 = State()
    encode_hex = State()
    encode_url = State()
    encode_rot13 = State()

class Decoder(StatesGroup):
    decode_base64 = State()
    decode_base32 = State()
    decode_hex = State()
    decode_url = State()
    decode_rot13 = State()

class CheckLeaks(StatesGroup):
    email = State()