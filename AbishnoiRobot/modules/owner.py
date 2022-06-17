from AbishnoiRobot import pbot as bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@bot.on_message(filters.command("owner"))
def command(bot, message):
    bot.send_message(message.chat.id,) 
    
    
             reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• ᴏᴡɴᴇʀ •", url="tg://user?id=1452219013"
                    
                                        ),
                ]
            ]
        ),
    )
