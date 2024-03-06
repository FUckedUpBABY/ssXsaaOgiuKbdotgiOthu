from pyrogram import Client, filters
from FUNC.usersdb_func import *
import threading
import asyncio


@Client.on_message(filters.command("viewbrod", [".", "/"]))
async def addbrod(Client, message):
    try:
        user_id = str(message.from_user.id)
        CEO = "5371579102"
        owner = "5371579102"
        sent_brod = 0
        not_sent = 0
        if user_id != CEO:
            resp = "𝙈𝙛 𝙔𝙤𝙪 𝙖𝙧𝙚 𝙉𝙤𝙩 𝙩𝙝𝙚 𝙊𝙬𝙣𝙚𝙧"
            msg1 = await message.reply_text(resp, message.id)
        else:
            getsk = open("FILES/brod.txt",encoding="UTF-8").read()
            sk = f"<b>{getsk}</b>"
            resp = f"""<b>
BOT CURRENT BRODCAST MEASAGE

{sk}
      </b>"""
            await message.reply_text(resp, message.id)
    except Exception as e:
        await message.reply_text(e, message.id)
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")
