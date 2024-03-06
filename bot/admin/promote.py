from pyrogram import Client, filters
from FUNC.usersdb_func import *


@Client.on_message(filters.command("pm", [".", "/"]))
async def cmd_pm(Client, message):
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
                time_of_pm = int(msg[2])
            except:
                user_id = message.reply_to_message.from_user.id
                time_of_pm = int(msg[1])
            pm_chk = getuserinfo(user_id)
            status = str(pm_chk["status"])
            if status != 'FREE':
                resp = f"""
  <a href="tg://user?id={user_id}">{user_id}</a> 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐔𝐬𝐞𝐫 𝐟𝐨𝐮𝐧𝐝 𝐢𝐧 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞✅.
        """
                await message.reply_text(resp, message.id)
            else:
                getpm(user_id,time_of_pm)
                resp = f"""
<a href="tg://user?id={user_id}">{user_id}</a> 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐔𝐬𝐞𝐫 𝐩𝐫𝐨𝐦𝐨𝐭𝐞𝐝 𝐢𝐧 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞 ✅.
𝐕𝐚𝐥𝐢𝐝 𝐭𝐢𝐥𝐥: {time_of_pm} 𝗗𝗮𝘆𝘀
        """
                await message.reply_text(resp, message.id)
                user_resp = f"""𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐔𝐬𝐞𝐫 𝐩𝐫𝐨𝐦𝐨𝐭𝐞𝐝 𝐢𝐧 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞 ✅
𝐕𝐚𝐥𝐢𝐝 𝐭𝐢𝐥𝐥: {time_of_pm} 𝗗𝗮𝘆𝘀"""
                await Client.send_message(user_id, user_resp)

    except Exception as e:
        await message.reply_text("USERS IS 𝐔𝐒𝐄𝐑 𝐍𝐎𝐓 𝐅𝐎𝐔𝐍𝐃 𝐈𝐍 𝐃𝐀𝐓𝐀𝐁𝐀𝐒𝐄.", message.id)
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")
