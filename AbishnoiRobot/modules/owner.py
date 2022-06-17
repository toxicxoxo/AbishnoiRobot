ffrom AbishnoiRobot import pbot as bot
from pyrogram import filters 
@bot.on_message(filters.command("owner"))
def command(bot, message):  
    bot.send_message(message.chat.id,"@Abishnoi1M")
                     reply_markupp=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• ᴏᴡɴᴇʀ •", url="tg://user?id=1452219013"),
                    InlineKeyboardButton(
                        "• sᴏᴜʀᴄᴇ •",
                        url="https://github.com/KingAbishnoi/AbishnoiRobot",
                    ),
                ]
            ]
        )
        ")
        
   
    
                     
