from pyrogram import Client, filters
from FUNC.usersdb_func import *


@Client.on_message(filters.command("info", [".", "/"]))
async def cmd_info(Client, message):
    try:
        user_id = str(message.from_user.id)
        plancheck = plan_expirychk(user_id)
        if plancheck == "YES":
            resp = """
𝐇𝐄𝐘 𝐁𝐎𝐙𝐎𝐎!
𝐏𝐋𝐀𝐍 𝐄𝐗𝐏𝐈𝐑𝐄𝐃 𝐁𝐀𝐁𝐘! 𝐁𝐔𝐘 /buy 𝐨𝐫 𝐁𝐄𝐆 @stripe_xD
      """
            await Client.send_message(user_id, resp)
        else:
            pass
        regdata = getuserinfo(user_id)
        results = str(regdata)
        if results == 'None':
            resp = "𝐔𝐧𝐫𝐞𝐠𝐢𝐬𝐭𝐞𝐫𝐞𝐝 𝐔𝐬𝐞𝐫. 𝐏𝐫𝐞𝐬𝐬 /register 𝐭𝐨 𝐮𝐬𝐞 𝐦𝐞."
            await message.reply_text(resp, message.id)
        else:

            if message.reply_to_message:
                #PLAN CHECK
                #await plan_expirychk(user_id)
                user_id = str(message.reply_to_message.from_user.id)
                username = str(message.reply_to_message.from_user.username)
                first_name = str(message.reply_to_message.from_user.first_name)
                info = getuserinfo(user_id)
                results = str(info)
                if results == "None":
                    send_info = f"""
𝐈𝐍𝐅𝐎 ⟿ 𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 𝐂𝐇𝐄𝐂𝐊𝐄𝐑 𝐁𝐎𝐓 𝐎𝐅 𝐓𝐄𝐀𝐌 𝐍𝐌𝐁
⊶⊶⊶
∎ 𝐅𝐈𝐑𝐒𝐓 𝐍𝐀𝐌𝐄 ⟿ {first_name}
∎ 𝐏𝐄𝐑𝐌𝐀𝐍𝐄𝐍𝐓 𝐈𝐃 ⟿ <code>{user_id}</code>
∎ 𝐂𝐔𝐑𝐑𝐄𝐍𝐓 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 ⟿ {username}
∎ 𝐏𝐄𝐑𝐌𝐀𝐍𝐄𝐍𝐓 𝐏𝐑𝐎𝐅𝐈𝐋𝐄 𝐋𝐈𝐍𝐊 ⟿ <a href="tg://user?id={message.reply_to_message.from_user.id}">Profile Link</a>
∎ 𝐂𝐔𝐑𝐑𝐄𝐍𝐓 𝐒𝐓𝐀𝐓𝐔𝐒 ⟿ 𝐔𝐒𝐄𝐑 𝐍𝐎𝐓 𝐅𝐎𝐔𝐍𝐃 𝐈𝐍 𝐃𝐀𝐓𝐀𝐁𝐀𝐒𝐄
∎ 𝐂𝐑𝐄𝐃𝐈𝐓𝐒 𝐋𝐄𝐅𝐓 ⟿ 𝐍/𝐀
∎ 𝐏𝐋𝐀𝐍 𝐕𝐀𝐋𝐈𝐃𝐈𝐓𝐘 ⟿ 𝐍/𝐀
"""
                    await message.reply_text(send_info, message.id)
                else:
                    #await plan_expirychk(pid)
                    info = getuserinfo(user_id)
                    results = info
                    status = results["status"]
                    plan = results["plan"]
                    expiry = results["expiry"]
                    credit = results["credit"]
                    antispam_time = results["antispam_time"]
                    totalkey = results["totalkey"]
                    reg_at = results["reg_at"]
                    send_info = f"""
𝐈𝐍𝐅𝐎 ⟿ 𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 𝐂𝐇𝐄𝐂𝐊𝐄𝐑 𝐁𝐎𝐓 𝐎𝐅 𝐓𝐄𝐀𝐌 𝐍𝐌𝐁
⊶⊶⊶
∎ 𝐅𝐈𝐑𝐒𝐓 𝐍𝐀𝐌𝐄 ⟿ {first_name}
∎ 𝐏𝐄𝐑𝐌𝐀𝐍𝐄𝐍𝐓 𝐈𝐃 ⟿ <code>{user_id}</code>
∎ 𝐂𝐔𝐑𝐑𝐄𝐍𝐓 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 ⟿ {username}
∎ 𝐏𝐄𝐑𝐌𝐀𝐍𝐄𝐍𝐓 𝐏𝐑𝐎𝐅𝐈𝐋𝐄 𝐋𝐈𝐍𝐊 ⟿ <a href="tg://user?id={message.reply_to_message.from_user.id}">Profile Link</a>
∎ 𝐂𝐔𝐑𝐑𝐄𝐍𝐓 𝐒𝐓𝐀𝐓𝐔𝐒 ⟿ {status}
∎ 𝐂𝐑𝐄𝐃𝐈𝐓𝐒 𝐋𝐄𝐅𝐓 ⟿ {credit}
∎ 𝐏𝐋𝐀𝐍 𝐕𝐀𝐋𝐈𝐃𝐈𝐓𝐘 ⟿ {expiry}
"""
                    await message.reply_text(send_info, message.id)
            else:
                user_id = str(message.from_user.id)
                #PLAN CHECK
                #await plan_expirychk(user_id)
                username = str(message.from_user.username)
                first_name = str(message.from_user.first_name)
                info = getuserinfo(user_id)
                results = str(info)
                if results == "None":
                    send_info = f"""
𝐈𝐍𝐅𝐎 ⟿ 𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 𝐂𝐇𝐄𝐂𝐊𝐄𝐑 𝐁𝐎𝐓 𝐎𝐅 𝐓𝐄𝐀𝐌 𝐍𝐌𝐁
⊶⊶⊶
∎ 𝐅𝐈𝐑𝐒𝐓 𝐍𝐀𝐌𝐄 ⟿ {first_name}
∎ 𝐏𝐄𝐑𝐌𝐀𝐍𝐄𝐍𝐓 𝐈𝐃 ⟿ <code>{user_id}</code>
∎ 𝐂𝐔𝐑𝐑𝐄𝐍𝐓 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 ⟿ {username}
∎ 𝐏𝐄𝐑𝐌𝐀𝐍𝐄𝐍𝐓 𝐏𝐑𝐎𝐅𝐈𝐋𝐄 𝐋𝐈𝐍𝐊 ⟿ <a href="tg://user?id={message.from_user.id}">Profile Link</a>
∎ 𝐂𝐔𝐑𝐑𝐄𝐍𝐓 𝐒𝐓𝐀𝐓𝐔𝐒 ⟿ 𝐔𝐒𝐄𝐑 𝐍𝐎𝐓 𝐅𝐎𝐔𝐍𝐃 𝐈𝐍 𝐃𝐀𝐓𝐀𝐁𝐀𝐒𝐄
∎ 𝐂𝐑𝐄𝐃𝐈𝐓𝐒 𝐋𝐄𝐅𝐓 ⟿ 𝐍/𝐀
∎ 𝐏𝐋𝐀𝐍 𝐕𝐀𝐋𝐈𝐃𝐈𝐓𝐘 ⟿ 𝐍/𝐀
"""
                    await message.reply_text(send_info, message.id)
                else:
                    #await plan_expirychk(user_id)
                    info = getuserinfo(user_id)
                    results = info
                    status = results["status"]
                    plan = results["plan"]
                    expiry = results["expiry"]
                    credit = results["credit"]
                    antispam_time = results["antispam_time"]
                    totalkey = results["totalkey"]
                    reg_at = results["reg_at"]
                    send_info = f"""
𝐈𝐍𝐅𝐎 ⟿ 𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 𝐂𝐇𝐄𝐂𝐊𝐄𝐑 𝐁𝐎𝐓 𝐎𝐅 𝐓𝐄𝐀𝐌 𝐍𝐌𝐁
⊶⊶⊶
∎ 𝐅𝐈𝐑𝐒𝐓 𝐍𝐀𝐌𝐄 ⟿ {first_name}
∎ 𝐏𝐄𝐑𝐌𝐀𝐍𝐄𝐍𝐓 𝐈𝐃 ⟿ <code>{user_id}</code>
∎ 𝐂𝐔𝐑𝐑𝐄𝐍𝐓 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 ⟿ {username}
∎ 𝐏𝐄𝐑𝐌𝐀𝐍𝐄𝐍𝐓 𝐏𝐑𝐎𝐅𝐈𝐋𝐄 𝐋𝐈𝐍𝐊 ⟿ <a href="tg://user?id={message.from_user.id}">Profile Link</a>
∎ 𝐂𝐔𝐑𝐑𝐄𝐍𝐓 𝐒𝐓𝐀𝐓𝐔𝐒 ⟿ {status}
∎ 𝐂𝐑𝐄𝐃𝐈𝐓𝐒 𝐋𝐄𝐅𝐓 ⟿ {credit}
∎ 𝐏𝐋𝐀𝐍 𝐕𝐀𝐋𝐈𝐃𝐈𝐓𝐘 ⟿ {expiry}
  """
                await message.reply_text(send_info, message.id)
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")
