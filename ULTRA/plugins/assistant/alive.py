# COPYRIGHT (C) 2021-2022 BY MONSTERX2
# modify by madboy482 and alain_champion

from MONSTER import bot
from MONSTERX import xbot, ID
import heroku3
from telethon import events
from MONSTER import StartTime
import time
import datetime
from . import *
from telethon import events, Button, custom
import re, os
from MONSTERX import PHOTO, xbot, BOT, VERSION
from MONSTER import bot
@xbot.on(events.NewMessage(pattern=("/alive")))
async def awake(event):
  MONSTERX = f"Hᴇʟʟᴏ !! Tʜɪs ɪs **{BOT}**\n\n"
  MONSTERX += "**Aʟʟ sʏsᴛᴇᴍs ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ...**\n\n"
  MONSTERX += f"**{BOT} Vᴇʀsɪᴏɴ** : `{VERSION}`\n\n"
  MONSTERX += f"**Usᴇʀ** : @{bot.me.username}\n\n"
  MONSTERX += "**Fᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ ʙᴏᴛ...**\n\n"
  MONSTERX += "**Tᴇʟᴇᴛʜᴏɴ** : `1.20`\n\n"
  MONSTERX += "~~ **Tʜᴀɴᴋs ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ᴍᴇ** !!"
  BUTTON = [[Button.url("Mᴀsᴛᴇʀ", f"https://t.me/{bot.me.username}"), Button.url(f"{BOT} Rᴇᴘᴏ", "https://github.com/MONSTER-OP/MONSTER-X")]]
  BUTTON += [[custom.Button.inline("Rᴇᴘᴏsɪᴛᴏʀɪᴇs »»", data="MONSTERX")]]
  await xbot.send_file(event.chat_id, PHOTO, caption=MONSTERX,  buttons=BUTTON)




@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"MONSTERX")))
async def callback_query_handler(event):
# inline by MONSTERX2 and PROBOY22 🔥
  PROBOYX = [[Button.url("Rᴇᴘᴏ UʟᴛʀᴀX", "https://github.com/MONSTER-OP/MONSTER-X")]]
  PROBOYX +=[[Button.url("Dᴇᴘʟᴏʏ UʟᴛʀᴀX", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FMONSTER-OP%2FHEROKU&template=https%3A%2F%2Fgithub.com%2FMONSTER-OP%2FHEROKU")]]
  PROBOYX +=[[Button.url("Tᴜᴛᴏʀɪᴀʟ", "https://youtu.be/rGCSSFPsS4Q"), Button.url("Sᴛʀɪɴɢ Sᴇssɪᴏɴ", "https://replit.com/@MONSTERX2/MONSTER-X#main.py")]]
  PROBOYX +=[[Button.url("Aᴘɪ Iᴅ & Aᴘɪ Hᴀsʜ", "https://t.me/usetgxbot"), Button.url("Rᴇᴅɪs", "https://redislabs.com")]]
  PROBOYX +=[[Button.url("Sᴜᴘᴘᴏʀᴛ Cʜᴀɴɴᴇʟ", "https://t.me/MONSTERXOT"), Button.url("Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ", "https://t.me/MONSTERXChat")]]
  PROBOYX +=[[custom.Button.inline("«« Aʟɪᴠᴇ", data="PROBOY")]]
  await event.edit(text=f"Aʟʟ Dᴇᴛᴀɪʟs Oғ Rᴇᴘᴏs", buttons=PROBOYX)


@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"PROBOY")))
async def callback_query_handler(event):
# inline by MONSTERX2 and PROBOY22 🔥
  MONSTERX = f"Hᴇʟʟᴏ !! Tʜɪs ɪs **{BOT}**\n\n"
  MONSTERX += "**Aʟʟ sʏsᴛᴇᴍs ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ...**\n\n"
  MONSTERX += f"**{BOT} Vᴇʀsɪᴏɴ** : `{VERSION}`\n\n"
  MONSTERX += f"**Usᴇʀ** : @{bot.me.username}\n\n"
  MONSTERX += "**Fᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ ʙᴏᴛ...**\n\n"
  MONSTERX += "**Tᴇʟᴇᴛʜᴏɴ** : `1.20`\n\n"
  MONSTERX += "~~ **Tʜᴀɴᴋs ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ᴍᴇ** !!"
  BUTTONS = [[Button.url("Mᴀsᴛᴇʀ", f"https://t.me/{bot.me.username}"), Button.url(f"{BOT} Rᴇᴘᴏ", "https://github.com/MONSTER-OP/MONSTER-X")]]
  BUTTONS += [[custom.Button.inline("Rᴇᴘᴏsɪᴛᴏʀɪᴇs »»", data="MONSTERX")]]
  await event.edit(text=MONSTERX, buttons=BUTTONS)


@xbot.on(events.NewMessage(pattern=("/repo")))
async def repo(event):
  await xbot.send_message(event.chat, "**Hᴇʀᴇ Is Tʜᴇ Rᴇᴘᴏ Fᴏʀ υℓтяα χ Usᴇʀʙᴏᴛ** \n\nFᴏʀ Aɴʏ Hᴇʟᴘ :- @MONSTERXOT", buttons=[[Button.url("⚜️ Rᴇᴘᴏ ⚜️", "https://github.com/MONSTER-OP/MONSTER-X"), Button.url("🔰 Dᴇᴘʟᴏʏ 🔰", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FMONSTER-OP%2FHEROKU&template=https%3A%2F%2Fgithub.com%2FMONSTER-OP%2FHEROKU")]])


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@xbot.on(events.NewMessage(pattern=None))
async def ok(event):
    msg = str(event.text)
    if not msg == "/ping":
     return

    start_time = datetime.datetime.now()
    message = await event.reply("_.._.._Pinging_.._.._")
    end_time = datetime.datetime.now()
    pingtime = end_time - start_time
    telegram_ping = str(round(pingtime.total_seconds(), 2)) + "s"
    uptime = get_readable_time((time.time() - StartTime))
    await message.edit(
        "<b><i>☞ Pᴏɴɢ !!</i></b>\n"
        "<b>➥ Tɪᴍᴇ Tᴀᴋᴇɴ:</b> <code>{}</code>\n"
        "<b>➥ Sᴇʀᴠɪᴄᴇ Uᴘᴛɪᴍᴇ:</b> <code>{}</code>".format(telegram_ping, uptime),
        parse_mode="html",
    )
