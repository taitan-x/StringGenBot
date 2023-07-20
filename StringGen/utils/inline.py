from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT


keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="𝐆ᴇɴᴇʀᴀᴛᴇ 𝐒ᴇssɪᴏɴ", callback_data="gensession")],
        [
            InlineKeyboardButton(text="𝐒ᴜᴘᴘᴏʀᴛ", url=SUPPORT_CHAT),
            InlineKeyboardButton(
                text="♕︎ 𝐎ᴡɴᴇʀ ♕︎", url="https://t.me/taitangamer"
            ),
        ],
    ]
)

gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="𝐏ʏʀᴏɢʀᴀᴍ v1", callback_data="pyrogram1"),
            InlineKeyboardButton(text="𝐏ʏʀᴏɢʀᴀᴍ v2", callback_data="pyrogram"),
        ],
        [InlineKeyboardButton(text="𝐓ᴇʟᴇᴛʜᴏɴ", callback_data="telethon")],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="ᴛʀʏ ᴀɢᴀɪɴ", callback_data="gensession")]]
)
