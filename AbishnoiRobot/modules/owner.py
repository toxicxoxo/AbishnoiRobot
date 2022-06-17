# Code By Asad Deliver To Abɪsʜɴᴏɪ (ᴛʜᴀɴᴋs ᴀsᴀᴅ ᴅᴇʟɪᴠᴇʀ  )
# © Alexa_Help


import asyncio
from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,                             InlineKeyboardMarkup, InputMediaPhoto, Message)
from AbishnoiRobot import pbot as bot

   AK = "https://telegra.ph/file/348fd99cf32b44153f5c1.jpg"



    @bot.on_message(filters.command(["owner", "noob"]))
    async def owner(bot, message):
    await message.reply_photo(
          photo=AK,
          caption=f"""**ʜᴇʏ {message.from_user.mention()},\n\nɪ ᴀᴍ [「 ᴀʙɢ 𒆜 ʀᴏʙᴏᴛ 」](t.me/Abishnoi_ro_bot)**


      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• ᴏᴡɴᴇʀ •", url="tg://user?id=1452219013",
                  
                     
                    ),
                ]
            ]
        ),
    )

