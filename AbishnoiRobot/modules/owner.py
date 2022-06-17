

  from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
  from AbishnoiRobot import pbot as bot
  from pyrogram import filters


   AK = "https://telegra.ph/file/348fd99cf32b44153f5c1.jpg"



    @client.on_message(filters.command(["owner", "noob"]))
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


