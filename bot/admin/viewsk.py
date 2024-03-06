from pyrogram import Client, filters
from FUNC.usersdb_func import *
import os

@Client.on_message(filters.command("viewsk", [".", "/"]))
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
            if os.path.getsize("FILES/sks.txt") == 0:
                resp = "NO SK ADDED CURRENTLY."
                await message.reply_text(resp, message.id)
            else:
                sks = open("FILES/sks.txt",encoding="UTF-8").read().splitlines()
                total = ""
                amt = 0
                for sk in sks:
                    amt += 1
                resp = f"""<b>
CURRENT SK ( {amt} )

<b>{open("FILES/sks.txt",encoding="UTF-8").read()}</b>
    </b>"""
                await message.reply_text(resp, message.id)
    except Exception as e:
        await message.reply_text(e, message.id)
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")
