      from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton   from pyrogram import filters   from AbishnoiRobot import pbot as client    
ABISHNOI = "https://telegra.ph/file/7bd111132fce009e4605e.jpg"  
@client.on_message(filters.command(["noob", "owner"]))
async def repo(client, message):     await message.reply_photo(         photo=ABISHNOI,         caption=f"""**ʜᴇʏ {message.from_user.mention()},\n\nɪ ᴀᴍ [「 ᴀʙɢ 𒆜 ʀᴏʙᴏᴛ 」](t.me/Abishnoi_ro_bot)**
""",         reply_markup=InlineKeyboardMarkup(             [                 [                     InlineKeyboardButton("• ᴏᴡɴᴇʀ •", url="tg://user?id=1452219013"),                     InlineKeyboardButton(                         "• sᴏᴜʀᴄᴇ •",                         url="https://github.com/KingAbishnoi/AbishnoiRobot",                     ),                 ]             ]         ),     )  
__mod_name__ = "Oᴡɴᴇʀ" 
