from pyrogram import Client, filters
from FUNC.usersdb_func import *


@Client.on_message(filters.command("pmlife", [".", "/"]))
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
            except:
                user_id = message.reply_to_message.from_user.id
            pm_chk = getuserinfo(user_id)
            status = str(pm_chk["status"])
            if status == '𝐏𝐞𝐫𝐦𝐚𝐧𝐞𝐧𝐭':
                resp = f"""
  <a href="tg://user?id={user_id}">{user_id}</a> 𝐟𝐨𝐮𝐧𝐝 𝐢𝐧 <b>𝐏𝐞𝐫𝐦𝐚𝐧𝐞𝐧𝐭</b> 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞.
        """
                await message.reply_text(resp, message.id)
            else:
                chk = getuserinfo(user_id)
                credit = int(chk["credit"])
                amt = credit + 50000
                pmlife(user_id,amt)
                resp = f"""
<a href="tg://user?id={user_id}">{user_id}</a> 𝗶𝘀 𝗽𝗿𝗼𝗺𝗼𝘁𝗲𝗱 𝘁𝗼 𝗮 <b>𝐏𝐞𝐫𝐦𝐚𝐧𝐞𝐧𝐭</b> 𝗠𝗲𝗺𝗯𝗲𝗿 ✅.
𝐕𝐚𝐥𝐢𝐝 𝐭𝐢𝐥𝐥: <b>LIFEIME</b>
𝗖𝗿𝗲𝗱𝗶𝘁 𝗔𝗱𝗱𝗲𝗱: 50,000
        """
                await message.reply_text(resp, message.id)
                user_resp = f"""𝗛𝗘𝗬 𝗗𝗨𝗗𝗘 ! 
𝗬𝗢𝗨𝗥 𝗔𝗖𝗖𝗢𝗨𝗡𝗧 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟𝗟𝗬 𝗣𝗥𝗢𝗠𝗢𝗧𝗘𝗗 𝗧𝗢 '<b>𝐏𝐞𝐫𝐦𝐚𝐧𝐞𝐧𝐭</b>' 𝗨𝗦𝗘𝗥 ✅
𝐕𝐚𝐥𝐢𝐝 𝐭𝐢𝐥𝐥: <b>LIFEIME</b>
𝗖𝗿𝗲𝗱𝗶𝘁 𝗔𝗱𝗱𝗲𝗱: 50,000"""
                await Client.send_message(user_id, user_resp)

    except Exception as e:
        await message.reply_text("USERS IS 𝐔𝐒𝐄𝐑 𝐍𝐎𝐓 𝐅𝐎𝐔𝐍𝐃 𝐈𝐍 𝐃𝐀𝐓𝐀𝐁𝐀𝐒𝐄.", message.id)
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")
