from AbishnoiRobot import pbot as bot
from pyrogram import filters 
@bot.on_message(filters.command("owner"))
def command(bot, message):  
    bot.send_message(message.chat.id,"@Abishnoi1M")
                     
