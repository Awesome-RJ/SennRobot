import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from KyyRobot.events import register
from KyyRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/875125db5a52bb1cba49e.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Nasty.** \n\n"
  TEXT += "✘ **I'm Working Properly** \n\n"
  TEXT += f"✘ **My Master : [Rizzu Senpai](https://t.me/xflyrzu)** \n\n"
  TEXT += f"✘ **Library Version :** `{telever}` \n\n"
  TEXT += f"✘ **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"✘ **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Iam Working Now🔥 **"
  BUTTON = [[Button.url("ʜᴇʟᴘ", "https://t.me/Sentapibot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/SenNotSupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
