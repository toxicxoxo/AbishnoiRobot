import asyncio
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    Message,
)


from AbishnoiRobot import pbot as bot

ABISHNOI = "https://telegra.ph/file/ec3d72893958f6495ad3b.jpg"


@bot.on_message(filters.command(["noob", "owner"]))
async def repo(client, message):
    await message.reply_photo(
        photo=ABISHNOI,
        caption=f"""**ʜᴇʏ {message.from_user.mention()},\n\nɪ ᴀᴍ [「HOMIES BOT」](t.me/HomiesAttendantbot)**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• ᴏᴡɴᴇʀ •", url="https://t.me/HomiesAttendant"),
                ]
            ]
        ),
    )


__mod_name__ = "Oᴡɴᴇʀ"
