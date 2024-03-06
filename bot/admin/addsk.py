from pyrogram import Client, filters
import os

@Client.on_message(filters.command("addsk", [".", "/"]))
async def addbrod(Client, message):
    try:
        user_id = str(message.from_user.id)
        admins = [
            "5371579102",
            "5833987727",
            "198809",
            "54950",
            "162972"
        ]
        if user_id not in admins:
            resp = "𝙈𝙛 𝙔𝙤𝙪 𝙖𝙧𝙚 𝙉𝙤𝙩 𝙩𝙝𝙚 𝙊𝙬𝙣𝙚𝙧"
            await message.reply_text(resp, message.id)
        else:
            sk = message.reply_to_message.text
            if os.path.getsize("FILES/sks.txt") == 0:
                with open("FILES/sks.txt", "a",encoding="UTF-8") as f:
                    f.write(sk)
            else:
                with open("FILES/sks.txt", "a",encoding="UTF-8") as f:
                    f.write(f"\n{sk}")
            resp = f"""<b>
𝐒𝐊 𝐔𝐏𝐃𝐀𝐓𝐄𝐃 ✅

SK: <code>{sk}</code>
      </b>"""
            await message.reply_text(resp, message.id)
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")
