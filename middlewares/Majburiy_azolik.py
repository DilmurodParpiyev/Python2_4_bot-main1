from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from utils.azolikni_tekshirish import tekshirish
from data.config import kanallar
from loader import bot



class Asosiy_checking(BaseMiddleware):
    async def on_pre_process_update(self,xabar:types.Update,data:dict):
        if xabar.message:
            user_id = xabar.message.from_user.id
        elif xabar.callback_query:
            user_id = xabar.callback_query.from_user.id
        else:
            return
        matn = 'Quyidagi kanalga azo boling\n'
        royxat = []
        daslabki_holati = True
        for k in kanallar:
            holat = await tekshirish(user_id=user_id,kanal_link=k)
            daslabki_holati *= holat

            kanal = await bot.get_chat(k)

            if not holat:
                link = await kanal.export_invite_link()
                button = [InlineKeyboardButton(text=f'Obuna bolish ❌',url=f"{link}")]
                royxat.append(button)
        royxat.append([InlineKeyboardButton(text="Tasdiqlash ✅",callback_data='www')])
        if not daslabki_holati:
            await bot.send_message(chat_id=user_id,text=matn,disable_web_page_preview=True,
                                       reply_markup=InlineKeyboardMarkup(inline_keyboard=royxat))
            raise CancelHandler()