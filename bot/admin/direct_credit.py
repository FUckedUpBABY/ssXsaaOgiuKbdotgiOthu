from pyrogram import Client, filters
from FUNC.usersdb_func import *


@Client.on_message(filters.command("ac", [".", "/"]))
async def cmd_ac(Client, message):
    try:
        user_id = str(message.from_user.id)
        CEO = "5371579102"
        if user_id != CEO:
            resp = "𝙈𝙛 𝙔𝙤𝙪 𝙖𝙧𝙚 𝙉𝙤𝙩 𝙩𝙝𝙚 𝙊𝙬𝙣𝙚𝙧"
            msg1 = await message.reply_text(resp, message.id)
        else:
            try:
                msg = message.text.split(" ")
                amt = int(msg[1])
                user_id = msg[2]
                chk = getuserinfo(user_id)
                credit = int(chk["credit"])
                resp = f"""<b>
        ID: <code>{user_id}</code>
Previous Credits: {credit}
After Credits Should Be : {credit+amt}
        </b>"""
                await message.reply_text(resp, message.id)
                value = credit + amt
                directcredit(user_id, value)
                resp = f"""
<code>{amt}</code> 𝐂𝐫𝐞𝐝𝐢𝐭 𝐆𝐢𝐟𝐭𝐞𝐝 𝐭𝐨 <a href="tg://user?id={user_id}">{user_id}</a> 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 ✅
        """
                await message.reply_text(resp, message.id)
                user_sms = f"""
𝗖𝗼𝗻𝗴𝗿𝗮𝘁𝘀 ! 
𝐂𝐨𝐧𝐠𝐨! 𝐘𝐨𝐮 𝐆𝐨𝐭 {amt} 𝗖𝗿𝗲𝗱𝗶𝘁𝘀 ✅

𝗧𝘆𝗽𝗲 /credits 𝐭𝐨 𝐠𝐞𝐭 𝐂𝐫𝐞𝐝𝐢𝐭𝐬 𝐢𝐧𝐟𝐨
        """
                await Client.send_message(user_id, user_sms)
                chk = getuserinfo(user_id)
                credit = int(chk["credit"])
                resp = f"""<b>
        ID: <code>{user_id}</code>
After Credits: {credit}
        </b>"""
                await message.reply_text(resp, message.id)
            except Exception as e:
                await message.reply_text(e, message.id)
    except Exception as e:
        await message.reply_text(e, message.id)
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")
