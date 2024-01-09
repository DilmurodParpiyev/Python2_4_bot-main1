from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

tillar_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="kino tanlamoq",callback_data='til1'),
        ],
        [
            InlineKeyboardButton(text="Ulashish",switch_inline_query='')
        ]
    ],

)