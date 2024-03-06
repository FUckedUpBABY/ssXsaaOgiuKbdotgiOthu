from pyrogram import Client, filters
from FUNC.usersdb_func import *


@Client.on_message(filters.command("add", [".", "/"]))
async def cmd_add(Client, message):
    try:
        user_id = str(message.from_user.id)
        CEO = "5371579102"
        if user_id != CEO:
            resp = "𝙈𝙛 𝙔𝙤𝙪 𝙖𝙧𝙚 𝙉𝙤𝙩 𝙩𝙝𝙚 𝙊𝙬𝙣𝙚𝙧"
            msg1 = await message.reply_text(resp, message.id)
        else:
            msg = message.text.split(" ")
            try:
                chat_id = str(msg[1])
            except:
                chat_id = str(message.chat.id)
            getchat = str(getchatinfo(chat_id))
            if getchat == "None":
                insert = addchat(chat_id)
                resp = f"""
𝐓𝐇𝐈𝐒 (<code>{chat_id}</code>) 𝐆𝐑𝐎𝐔𝐏 𝐀𝐔𝐓𝐇𝐎𝐑𝐙𝐈𝐄𝐃 ✅.
        """
                await message.reply_text(resp, message.id)
            else:
                find = str(getchatinfo(chat_id))
                if find != "None":
                    resp = f"""
𝐓𝐇𝐈𝐒 (<code>{chat_id}</code>) 𝐆𝐑𝐎𝐔𝐏 𝐃𝐄𝐀𝐔𝐓𝐇𝐎𝐑𝐙𝐈𝐄𝐃 ✅.
        """
                    await message.reply_text(resp, message.id)
                else:
                    return None

    except Exception as e:
        await message.reply_text(e, message.id)
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")
