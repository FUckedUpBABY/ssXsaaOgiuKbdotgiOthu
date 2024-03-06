from pyrogram import Client, filters
from FUNC.usersdb_func import *


@Client.on_message(filters.command("fr", [".", "/"]))
async def cmd_fr(Client, message):
    try:
        user_id = str(message.from_user.id)
        CEO = "5371579102"
        if user_id != CEO:
            resp = "𝙈𝙛 𝙔𝙤𝙪 𝙖𝙧𝙚 𝙉𝙤𝙩 𝙩𝙝𝙚 𝙊𝙬𝙣𝙚𝙧"
            msg1 = await message.reply_text(resp, message.id)
        else:
            msg = message.text.split(" ")
            try:
                user_id = str(msg[1])
            except:
                user_id = message.reply_to_message.from_user.id

            pm_chk = getuserinfo(user_id)
            status = str(pm_chk["status"])
            if status != 'PREMIUM':
                resp = f"""
<a href="tg://user?id={user_id}">{user_id}</a> 𝐟𝐨𝐮𝐧𝐝 𝐢𝐧 𝐟𝐫𝐞𝐞 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞 Lol.
          """
                await message.reply_text(resp, message.id)
            else:
                freeuser(user_id)
                resp = f"""
<a href="tg://user?id={user_id}">{user_id}</a> 𝐋𝐦𝐚𝐨 𝐝𝐞𝐦𝐨𝐭𝐞𝐝 𝐭𝐨 𝐟𝐫𝐞𝐞 ✅.
          """
                await message.reply_text(resp, message.id)
                user_resp = """𝐋𝐦𝐚𝐨 𝐝𝐞𝐦𝐨𝐭𝐞𝐝 𝐭𝐨 𝐟𝐫𝐞𝐞 ✅"""
                await Client.send_message(user_id, user_resp)

    except Exception as e:
        await message.reply_text(e, message.id)
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")
