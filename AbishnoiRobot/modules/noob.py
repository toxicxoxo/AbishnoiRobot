import asyncio
from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,                             InlineKeyboardMarkup, InputMediaPhoto, Message)


from AbishnoiRobot import pbot as bot
      
ABISHNOI = "https://telegra.ph/file/7bd111132fce009e4605e.jpg"  

@bot.on_message(filters.command(["noob", "owner"]))
async def repo(client, message):   
       await message.reply_photo(      
            photo=ABISHNOI,      
            caption=f"""**ʜᴇʏ {message.from_user.mention()},\n\nɪ ᴀᴍ [「 ᴀʙɢ 𒆜 ʀᴏʙᴏᴛ 」](t.me/Abishnoi_ro_bot)**
""",        
            reply_markup=InlineKeyboardMarkup(   
                  [          
                        [          
                              InlineKeyboardButton("• ᴏᴡɴᴇʀ •", url="tg://user?id=1452219013"),        
                              
                        ]     
                  ]      
            ),     
      
      
      
      
      
      )  
__mod_name__ = "Oᴡɴᴇʀ" 

