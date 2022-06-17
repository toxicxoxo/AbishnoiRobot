# Code By Asad Deliver To Abɪsʜɴᴏɪ (ᴛʜᴀɴᴋs ᴀsᴀᴅ ᴅᴇʟɪᴠᴇʀ  )
# © Alexa_Help

from AbishnoiRobot import pbot as bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@bot.on_message(filters.command("owner") & filters.private & ~filters.edited)
async def useradd(_, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/9df5e00ded2ef88341769.jpg",
        caption=f"""•ᴀʙɪsʜɴᴏɪ•""",
   reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴏᴡɴᴇʀ", url=f"https://t.me/Abishnoi1M")
                ]
                
           ]
        ),
    )
