from pyrogram import Client, filters
from FUNC.usersdb_func import *
import threading
import asyncio


@Client.on_message(filters.command("addbrod", [".", "/"]))
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
            brodtext = message.reply_to_message.text
            erase = open('FILES/brod.txt', 'w',encoding="UTF-8").close()
            with open("FILES/brod.txt", "a",encoding="UTF-8") as f:
                f.write(brodtext)
            resp = f"""
𝐁𝐑𝐎𝐀𝐃𝐂𝐀𝐒𝐓 𝐒𝐄𝐍𝐓 ✅.

MSG:
{brodtext}
      """
            await message.reply_text(resp, message.id)
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")
