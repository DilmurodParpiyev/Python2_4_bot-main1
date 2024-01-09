from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(f"uzur kino topilmadi yoki qandaydir xatolik ketdi⚙️ "
                         f"Kinoni telegram kanalimizdan izlab ko'ring yoki adminga murojat qiling👮‍♀️"
                         f"https://t.me/kinobazalive ")