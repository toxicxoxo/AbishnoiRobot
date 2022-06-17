from AbishnoiRobot import pbot as bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@bot.on_message(filters.command("owner"))
def command(bot, message):
    bot.send_message
    
                InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                            text="Owner🥀",
                            url=f"https://t.me/Abishnoi1M"),
                    )
                    
                ]
                
             ]
                  
                    
                     
