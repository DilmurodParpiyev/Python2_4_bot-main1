import datetime

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, \
    InlineKeyboardMarkup, LabeledPrice
from filters.shaxsiy_uchun import Shaxsiy
from loader import dp, base, bot
from keyboards.default.menu_uchun import menu_button
from keyboards.default.Ortga_uchun import orqaga_button
from keyboards.default.indskiy_kinolar import indskiy_button
from keyboards.default.fantastik_kinolar import fantastik_button
from keyboards.default.multfilm_uchun import multik_button
from keyboards.default.qiziqarli_kinolar import qiziqarli_button
from keyboards.default.ujas_kinolar import ujas_button
from keyboards.inline.tillar_uchun import tillar_buttons

@dp.message_handler(Shaxsiy(),CommandStart())
async def bot_start(message: types.Message):
    msg_id = message.message_id
    ism = message.from_user.first_name
    familya = message.from_user.last_name
    username = message.from_user.username
    user_id = message.from_user.id
    date = datetime.datetime.now()
    try:
        base.user_qoshish(ism=ism,tg_id=user_id,fam=familya,username=username,date=date)

    except Exception:
        pass
    await message.answer(f"""Assalomu alaykum !\n
Menga istalgan kino nomini yozing, men sizga topib beraman.\n

Yordam: /help
Random: /random
Mening kinolarim: /my
Top: /top
Kino qo`shish: /add, {message.from_user.full_name}!""",reply_markup=tillar_buttons)

    await bot.delete_message(chat_id=user_id,message_id=msg_id)

## BUTTON LAR
@dp.message_handler(text="Krilmasin xavfli")
async def bot_start(message: types.Message):
    manzil = "https://t.me/s4eft46tu5/22"
    user_id = message.from_user.id
    await bot.send_video(chat_id=user_id, video=manzil, caption="Dabba kirilmasin deyildiku")

@dp.message_handler(text="Don 1")
async def bot_start(message: types.Message):
    manzil = "https://t.me/kinobazalive/363"
    user_id = message.from_user.id
    await bot.send_video(chat_id=user_id, video=manzil, caption="  Don 1"
                                                                " Hajmi: 665.65 Mb")

@dp.message_handler(text="Don 2")
async def bot_start(message: types.Message):
    manzil = "https://t.me/kinobazalive/364"
    user_id = message.from_user.id
    await bot.send_video(chat_id=user_id, video=manzil, caption="  Don 2"
                                                                " Hajmi: 523.78 Mb")



@dp.message_handler(commands='reklama', chat_id='5883029982')
async def bot_start(message: types.Message):
    userlar = base.select_barcha_foydalanuvchilar()
    print(userlar)

    for user in userlar:
        await bot.send_message(chat_id=user[4],text="Bu reklama !!!")


@dp.callback_query_handler(text="til1")
async def bot_start(xabar: CallbackQuery):
    await xabar.message.answer(f"Mashxur kinolarni ushbu menyu dan tanlashingiz mumkin 🫴 ! {xabar.from_user.full_name}",
                               reply_markup=menu_button)

@dp.message_handler( text='Ortga')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id, text="Maxsulotni tanlang", reply_markup = menu_button)

@dp.callback_query_handler(text="www")
async def bot_start(xabar:CallbackQuery):
    await bot.delete_message(chat_id=xabar.from_user.id)# namuna

@dp.message_handler(text="yana🔓")
async def bot_start(message: types.Message):
    await message.answer(f"botdagi kinolar faqat menyu dagi kinolar bilan cheklanib qolmaydi."
                         f"Kino qidirmoqchi bo'lsangiz, uning nomini yoki ushbu kanaldagi qisqa kinolar"
                         f"ostidagi maxsus kodlarni bizning botga yuboring🫴 https://t.me/qorqinchili_va_qiziqarli_kinolar"
                         f" Agarda unda xam chiqmasa yoki botda xatolik ketsa menyu ostida"
                         f"👉 Adminga murojat 👈 tugmasi orqali kino qo'shtirishimgiz mumkin ", reply_markup=tillar_buttons)

@dp.message_handler(text="top qiziqarli kinolar🤩")
async def bot_start(message: types.Message):
    await message.answer(f"...", reply_markup=qiziqarli_button)

@dp.message_handler(text="top fantastik🦸")
async def bot_start(message: types.Message):
    await message.answer(f"...", reply_markup=fantastik_button)

@dp.message_handler(text="top ujas😱")
async def bot_start(message: types.Message):
    await message.answer(f"...", reply_markup=ujas_button)

@dp.message_handler(text="top india films🇮🇳")
async def bot_start(message: types.Message):
    await message.answer(f"...", reply_markup=indskiy_button)

@dp.message_handler(text="top multfilmlar🧸")
async def bot_start(message: types.Message):
    await message.answer(f"...", reply_markup=multik_button)

@dp.message_handler(text="🔙Orqaga")
async def bot_start(message: types.Message):
    await message.answer(f"...", reply_markup=menu_button)

@dp.message_handler(text="/add")
async def bot_start(message: types.Message):
    await message.answer(f"""Hozircha foydalanuchilar kino qo'shishi cheklangan!
Agarda kino qo'shmoqchi bo'lsangiz adminga yozing.

👤Admin: @Tezda_ustiga_bosing!""", reply_markup=menu_button)

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







menular = base.select_barcha_menular()

@dp.message_handler(text=[menu[1] for menu in menular])
async def bot_start(message: types.Message):
    menu_nomi = message.text
    tur = base.select_from_menu(nomi=menu_nomi)
    print(tur)
    tanlangan_menu = base.select_maxsulot(tur_id=tur[0])
    index = 0
    keys = []
    j = 0
    for menu in tanlangan_menu:
        if j % 2 == 0 and j != 0:
            index += 1
        if j % 2 == 0:
            keys.append([KeyboardButton(text=f'{menu[0]}', )])
        else:
            keys[index].append(KeyboardButton(text=f'{menu[0]}', ))
        j += 1

    keys.append([KeyboardButton(text='🔙Orqaga')])
    menu_buttons = ReplyKeyboardMarkup(keyboard=keys, resize_keyboard=True)
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id,text="Maxsulotni tanlang",reply_markup=menu_buttons)



menular = base.select_barcha_maxsulotlar()
print(menular,)
@dp.message_handler( text=[menu[1] for menu in menular])
async def bot_start(message: types.Message):
    text = message.text
    print(text)
    """(1, 'Osh', 'https://t.me/UstozShogird/25032', 20000, None, 'Taomlar')"""
    maxsulot = base.select_maxsulot(nomi=text)
    max_id= maxsulot[0]
    max_nomi = maxsulot[1]
    max_rasmi = maxsulot[2]
    max_text = maxsulot[4]
    user_id = message.from_user.id
    malumot = f"Nomi : {max_nomi}\n" \
              f"Malumot :  {max_text}"

    await bot.send_photo(chat_id=user_id,photo=max_rasmi,caption=malumot,
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Sotib olish",callback_data=f"buy {max_id}")
            ]
        ]))




@dp.callback_query_handler()
async def bot_start(xabar: CallbackQuery):
    malumot = xabar.data.split()
    max_id = malumot[1]
    msg_id = xabar.message.message_id
    """['buy', '1']"""
    if malumot[0]=='buy':

        max_id = malumot[1]
        maxsulot = base.select_maxsulot(id=max_id)
        "(1, 'Osh', 'https://t.me/UstozShogird/26311', 14000, '', 1)"
        max_nomi = maxsulot[1]
        max_rasm = maxsulot[2]
        max_soni = 1
        ism  =xabar.from_user.full_name
        korzinka_maxsulot = base.select_maxsulot_from_korzinka(nomi=max_nomi)
        print(korzinka_maxsulot)
        if korzinka_maxsulot:
            soni = korzinka_maxsulot[0]+1
            print(soni,'ddddddddd')
            base.update_korzinka(nomi=max_nomi,son=soni)
        else:
            base.add_to_korzinka(ism=ism,nomi=max_nomi,rasm=max_rasm,son=max_soni)
        print(maxsulot)
        await xabar.message.answer(f"Sotib olindi !",
                               )

    elif malumot[0]=="minus":
        print(malumot)
        msg_id = xabar.message.message_id
        max_id = int(malumot[1])
        maxsulot = base.select_maxsulotlar_from_korzinka(id=max_id)[0]
        print(maxsulot)
        "(1, 'Osh', 'https://t.me/UstozShogird/26311', 14000, '', 1)"
        max_nomi = maxsulot[1]
        tg_id = xabar.from_user.id
        korzinka_maxsulot = base.select_maxsulot_from_korzinka(tg_id=tg_id, nomi=max_nomi)
        if korzinka_maxsulot:
            soni = korzinka_maxsulot[0] - 1
            base.update_korzinka(tg_id=tg_id, nomi=max_nomi, son=soni)
            await bot.edit_message_reply_markup(chat_id=tg_id,message_id=msg_id,reply_markup=InlineKeyboardMarkup(
               inline_keyboard=[
                   [
                       InlineKeyboardButton(text="-",callback_data=f"minus {max_id}"),
                       InlineKeyboardButton(text=f"{soni}" ,callback_data=f"num {max_id}"),
                       InlineKeyboardButton(text=f"+",callback_data=f"plus {max_id}")
                   ],
                   [
                       InlineKeyboardButton(text="Delete",callback_data=f"del {max_id}"),
                       InlineKeyboardButton(text="Xarid qilish",callback_data=f"shop {max_id}")
                   ]
               ]))

    elif malumot[0]=="plus":
        print(malumot)
        msg_id = xabar.message.message_id
        max_id = int(malumot[1])
        maxsulot = base.select_maxsulotlar_from_korzinka(id=max_id)[0]
        print(maxsulot)
        "(1, 'Osh', 'https://t.me/UstozShogird/26311', 14000, '', 1)"
        max_nomi = maxsulot[1]
        tg_id = xabar.from_user.id
        korzinka_maxsulot = base.select_maxsulot_from_korzinka(tg_id=tg_id, nomi=max_nomi)
        if korzinka_maxsulot:
            soni = korzinka_maxsulot[0] + 1
            base.update_korzinka(tg_id=tg_id, nomi=max_nomi, son=soni)
            await bot.edit_message_reply_markup(chat_id=tg_id,message_id=msg_id,reply_markup=InlineKeyboardMarkup(
               inline_keyboard=[
                   [
                       InlineKeyboardButton(text="-",callback_data=f"minus {max_id}"),
                       InlineKeyboardButton(text=f"{soni}" ,callback_data=f"num {max_id}"),
                       InlineKeyboardButton(text=f"+",callback_data=f"plus {max_id}")
                   ],
                   [
                       InlineKeyboardButton(text="Delete",callback_data=f"del {max_id}"),
                       InlineKeyboardButton(text="Xarid qilish", callback_data=f"shop {max_id}")
                   ]
               ]))

    elif malumot[0]=='del':
        base.delete_maxsulot_from_korzinka(id=max_id)
        await bot.delete_message(chat_id=xabar.from_user.id,message_id=msg_id)

    elif malumot[0] =='shop':
        maxsulot = base.select_maxsulotlar_from_korzinka(id=max_id)[0]
        """ (3, 'Osh', 'https://t.me/UstozShogird/26311', 14000, 4, 5883029982, '.....') """
        max_id = maxsulot[0]
        max_nomi = maxsulot[1]
        max_narxi = maxsulot[3]
        max_soni = maxsulot[4]
        summa = int(max_narxi)*int(max_soni)*100
        user_id = xabar.from_user.id
        await bot.send_invoice(chat_id=user_id,title="Sotib olingan maxsulot",
                               provider_token='371317599:TEST:1679139695376',currency='UZS',
                               description="Sotib olindi",
                               payload='111',
                               prices=[LabeledPrice(max_nomi,summa,),])


@dp.message_handler(Shaxsiy(),text="Korzinka")
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


