from data.config import ADMINS
from loader import dp,bot
from aiogram import types,F
from aiogram.filters import Command
from states.mystates import RegisterGroup
from aiogram.fsm.context import FSMContext
from keyboards.inline.buttons import button,CheckCall
@dp.message(Command('register'))
async def get_name(message:types.Message,state:FSMContext):
    await message.answer("Ismingizni kiriting!\n"
                         "Masalan:Behzod")
    await state.set_state(RegisterGroup.name)
@dp.message(F.text,RegisterGroup.name)
async def get_age(message:types.Message,state:FSMContext):
    name = message.text
    await state.update_data({
        'name':name
    })
    await message.answer("Yoshigizni kiriting!\n"
                         "Masalan:23")
    await state.set_state(RegisterGroup.age)
@dp.message(F.text,RegisterGroup.age)
async def get_job(message:types.Message,state:FSMContext):
    age = message.text
    await state.update_data({
        'age':age
    })
    await message.answer("Kasbingini kiriting!\n"
                         "Masalan:Quruvchi")
    await state.set_state(RegisterGroup.job)
@dp.message(F.text,RegisterGroup.job)
async def final(message:types.Message,state:FSMContext):
    job = message.text
    await state.update_data({
        'job':job
    })
    data = await state.get_data()
    text = (f"Ushbu malumotlar to'g'rimi?\n"
        f"<b>Ism</b>:{data['name']}\n"
            f"<b>Yosh</b>:{data['age']}\n"
            f"<b>Kasb</b>:{data['job']}")
    await message.answer(text,reply_markup=button.as_markup())
    await state.set_state(RegisterGroup.check)
@dp.callback_query(CheckCall.filter(),RegisterGroup.check)
async def get_check(call:types.CallbackQuery,callback_data:CheckCall,state:FSMContext):
    check = callback_data.checks
    await call.answer(cache_time=60)
    if check:
        data = await state.get_data()
        text = (
                f"<b>Ism</b>:{data['name']}\n"
                f"<b>Yosh</b>:{data['age']}\n"
                f"<b>Kasb</b>:{data['job']}")
        await bot.send_message(chat_id=ADMINS[0],text=text)
        await call.message.answer("Xabar adminga yuborildi!")
    else:
        await call.message.answer("Xabar adminga yuborilmadi!")
    await call.message.delete()
    await state.clear()



