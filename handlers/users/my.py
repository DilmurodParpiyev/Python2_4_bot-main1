from aiogram import types
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from loader import dp, bot, base
@dp.message_handler(text="/my")
async def bot_start(message: types.Message):
   user_id = message.from_user.id
   tanlangan_maxsulotlar = base.select_maxsulotlar_from_korzinka(tg_id=user_id)

   for maxsulot in tanlangan_maxsulotlar:
       """(3, 'Osh', 'https://t.me/UstozShogird/26311', 14000, 5, 5883029982, '.....')"""
       max_id = maxsulot[0]
       max_nomi = maxsulot[1]
       max_narxi = maxsulot[3]
       max_soni = maxsulot[4]
       max_rasm = maxsulot[2]
       await bot.send_photo(chat_id=user_id,photo=max_rasm,caption=f"Nomi : {max_nomi}\n"
                                                                   f"Narxi : {max_narxi}\n"
                                                                   f"Soni : {max_soni}\n"
        ,reply_markup=InlineKeyboardMarkup(
               inline_keyboard=[
                   [
                       InlineKeyboardButton(text="-",callback_data=f"minus {max_id}"),
                       InlineKeyboardButton(text=f"{max_soni}" ,callback_data=f"num {max_id}"),
                       InlineKeyboardButton(text=f"+",callback_data=f"plus {max_id}")
                   ],
                   [
                       InlineKeyboardButton(text="Delete",callback_data=f"del {max_id}"),
                       InlineKeyboardButton(text="Xarid qilish", callback_data=f"shop {max_id}")
                   ]
               ]))
