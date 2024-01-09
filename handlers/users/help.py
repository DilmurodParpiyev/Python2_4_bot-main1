from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("""Bu bot sizga Kino qidirishda yordam beradi shunchaki nomini yozsangiz bo'ldi va qidiruv turini tanlang keyin esa kerakli natijani oling.

1️⃣ Kino nomini to'liq yozish shart emas. 
Kino nomidagi biror so'zni kiriting.
Masalan:  'Kalmar o'yini' kinosini qidirish usuli

✅To'gri: Kalmar
✅To'gri: o'yini
✅To'gri: O'yini


❌Noto'g'ri: Kalmar-  o'yini
❌Noto'g'ri:  Kalmar --o'yini""")
    
    await message.answer("".join(text))
