from telethon import events, Button, custom, version
from telethon.tl.types import ChannelParticipantsAdmins
import asyncio
import os, re
import requests
import datetime
import time
from datetime import datetime
import random
from PIL import Image
from io import BytesIO
from AbishnoiRobot import telethn as bot
from AbishnoiRobot import telethn as tgbot
from AbishnoiRobot.events import register
from AbishnoiRobot import dispatcher


edit_time = 5
""" =======================HOMIES BOT====================== """
file1 = "https://telegra.ph/file/ff1a85057ef19a2e9f5c4.jpg"
file2 = "https://telegra.ph/file/3f08027fa00cbe727a515.jpg"
file3 = "https://telegra.ph/file/df52ba7b1783a2ee2cb97.jpg"
file4 = "https://telegra.ph/file/7e410e1ccaec5c47ef6e1.jpg"
file5 = "https://telegra.ph/file/fe8c6da35023c67ba1e66.jpg"
""" =======================HOMIES BOT====================== """


@register(pattern="/myinfo")
async def proboyx(event):
    chat = await event.get_chat()
    current_time = datetime.utcnow()
    firstname = event.sender.first_name
    button = [[custom.Button.inline("information", data="informations")]]
    on = await bot.send_file(
        event.chat_id,
        file=file2,
        caption=f"ʜᴇʏ  {firstname}, \n Cʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴ  \n ᴛᴏ ɢᴇᴛ ɪɴғᴏ ᴀʙᴏᴜᴛ ʏᴏᴜ ",
        buttons=button,
    )

    await asyncio.sleep(edit_time)
    ok = await bot.edit_message(event.chat_id, on, file=file3, buttons=button)

    await asyncio.sleep(edit_time)
    ok2 = await bot.edit_message(event.chat_id, ok, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok3 = await bot.edit_message(event.chat_id, ok2, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)

    await asyncio.sleep(edit_time)
    ok4 = await bot.edit_message(event.chat_id, ok3, file=file2, buttons=button)

    await asyncio.sleep(edit_time)
    ok5 = await bot.edit_message(event.chat_id, ok4, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok6 = await bot.edit_message(event.chat_id, ok5, file=file3, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"information")))
async def callback_query_handler(event):
    try:
        boy = event.sender_id
        PRO = await bot.get_entity(boy)
        LILIE = "Pᴏᴡᴇʀᴅ ʙʏ Aʙɪsʜɴᴏɪ  \n\n"
        LILIE += f"ғɪʀsᴛ ɴᴀᴍᴇ  : {PRO.first_name} \n"
        LILIE += f"ʟᴀsᴛ ɴᴀᴍᴇ  : {PRO.last_name}\n"
        LILIE += f"ʏᴏᴜ ʙᴏᴛ  : {PRO.bot} \n"
        LILIE += f"ʀᴇsᴛɪᴄᴛᴇᴅ  : {PRO.restricted} \n"
        LILIE += f"ʏᴏᴜʀ ɪᴅ  : {boy}\n"
        LILIE += f"ᴜsᴇʀɴᴀᴍᴇ : {PRO.username}\n"
        await event.answer(LILIE, alert=True)
    except Exception as e:
        await event.reply(f"{e}")


__command_list__ = ["myinfo"]
