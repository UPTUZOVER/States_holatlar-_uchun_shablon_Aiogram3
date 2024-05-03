from aiogram.filters.state import State, StatesGroup
class RegisterGroup(StatesGroup):
    name = State()
    age = State()
    job  = State()
    check = State()