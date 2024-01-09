from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.menu_uchun import menu_button
from keyboards.default.tasdiqlash_uchun import tasdiqlash_buttons
from loader import dp,bot
from states.Murojaat_uchun import Forma

# Echo bot
@dp.message_handler(text="Adminga murojat👮‍♂️")
async def bot_echo(message: types.Message):
  await message.answer(text="Ismni kiriting...")
  await Forma.ism_qabul_qilish_holati.set()




@dp.message_handler(state=Forma.ism_qabul_qilish_holati)
async def bot_start(message: types.Message,state:FSMContext):
    ism = message.text
    await state.update_data({"name":ism})

    await message.answer(f"yoshni kiriting ...")
    await Forma.yosh_qabul_qilish_holati.set()




@dp.message_handler(state=Forma.yosh_qabul_qilish_holati)
async def bot_start(message: types.Message, state: FSMContext):
       yoshi  = message.text
       await state.update_data({"yosh": yoshi})

       await message.answer(f"Telefon no'meringizni kiriting ...")
       await Forma.tel_qabul_qilish_holati.set()


@dp.message_handler(state=Forma.tel_qabul_qilish_holati)
async def bot_start(message: types.Message, state: FSMContext):
        nomer= message.text
        await state.update_data({"tel": nomer})

        await message.answer(f"kamchilik haqida ochiqroq yozing ...")
        await Forma.msg_qabul_qilish_holati.set()


@dp.message_handler(state=Forma.msg_qabul_qilish_holati)
async def bot_start(message: types.Message, state: FSMContext):
       matn = message.text
       await state.update_data({"text": matn})

       user_id = message.from_user.id


       malumot = await state.get_data()

       ismi = malumot.get('name')
       yoshi = malumot.get('yosh')
       teli = malumot.get('tel')
       murojaati = malumot.get('text')

       text = f"Ism : {ismi}\n" \
              f"Yosh : {yoshi}\n" \
              f"Tel : {teli}\n" \
              f"Murojaat : {murojaati}\n"

       await bot.send_message(chat_id=user_id,text=text,reply_markup=tasdiqlash_buttons)
       await Forma.tasdiqlash_holati.set()

@dp.message_handler(state=Forma.tasdiqlash_holati,text='🔙bekor qilish')
async def bot_start(message: types.Message, state: FSMContext):

        await message.answer(f"Bekor qilindi",reply_markup=menu_button)
        await state.finish()


@dp.message_handler(state=Forma.tasdiqlash_holati, text='Yuborish📤')
async def bot_start(message: types.Message, state: FSMContext):
    malumot = await state.get_data()
    user_id = message.from_user.id
    ismi = malumot.get('name')
    yoshi = malumot.get('yosh')
    teli = malumot.get('tel')
    murojaati = malumot.get('text')

    text = f"Ism : {ismi}\n" \
           f"Yosh : {yoshi}\n" \
           f"Tel : {teli}\n" \
           f"Murojaat : {murojaati}\n\n" \
           f"Murojaat egasi : {message.from_user.full_name}"
    await bot.send_message(chat_id='5955925106',text=text)
    await bot.send_message(chat_id=user_id,text="Adminga yuborildi",reply_markup=menu_button)
    await state.finish()

