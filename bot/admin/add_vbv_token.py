from pyrogram import Client, filters
from FUNC.usersdb_func import *



@Client.on_message(filters.command("addtoken", [".", "/"]))
async def addbrod(Client, message):
    try:
        user_id = str(message.from_user.id)
        CEO = "5371579102"
        if user_id != CEO:
            resp = "𝙈𝙛 𝙔𝙤𝙪 𝙖𝙧𝙚 𝙉𝙤𝙩 𝙩𝙝𝙚 𝙊𝙬𝙣𝙚𝙧"
            msg1 = await message.reply_text(resp, message.id)
        else:
            brodtext = message.reply_to_message.text
            erase = open('FILES/vbv_token.txt', 'w',encoding="UTF-8").close()
            with open("FILES/vbv_token.txt", "a",encoding="UTF-8") as f:
                f.write(brodtext)
            resp = f"""<b>
𝐕𝐁𝐕 𝐓𝐎𝐊𝐄𝐍 𝐇𝐀𝐒 𝐁𝐄𝐄𝐍 𝐔𝐏𝐃𝐀𝐓𝐄𝐃 ✅

SK: <code>{brodtext}</code>
      </b>"""
            await message.reply_text(resp, message.id)
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")
