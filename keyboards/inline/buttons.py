from aiogram.utils.keyboard import InlineKeyboardBuilder,InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData
class CheckCall(CallbackData,prefix='ikb'):
    checks:bool
button = InlineKeyboardBuilder()
button.button(text="✅ Ha",callback_data=CheckCall(checks=True))
button.button(text="❌ Yo'q",callback_data=CheckCall(checks=False))
button.adjust(2)