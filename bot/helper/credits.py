#IMPORT PYROGRAM MODULE
from pyrogram import Client, filters
#Reg Data Import
from FUNC.usersdb_func import *


@Client.on_message(filters.command("credits", [".", "/"]))
async def cmd_credit(Client, message):
    try:
        user_id = str(message.from_user.id)
        chat_type = str(message.chat.type)
        chat_id = str(message.chat.id)
        regdata = str(getuserinfo(user_id))
        if regdata == 'None':
            resp = "𝐔𝐧𝐫𝐞𝐠𝐢𝐬𝐭𝐞𝐫𝐞𝐝 𝐔𝐬𝐞𝐫. 𝐏𝐫𝐞𝐬𝐬 /register 𝐭𝐨 𝐮𝐬𝐞 𝐦𝐞."
            await message.reply_text(resp, message.id)
        else:
            getuser = getuserinfo(user_id)
            status = getuser["status"]
            role = status
            plan = getuser["plan"]
            expiry = getuser["expiry"]
            credit = int(getuser["credit"])
            antispam_time = int(getuser["antispam_time"])
            first_name = str(message.from_user.first_name)
            resp = f"""
𝐍𝐀𝐌𝐄 ⟿ {first_name}
𝐂𝐑𝐄𝐃𝐈𝐓𝐒 𝐋𝐄𝐅𝐓 ⟿ {credit}
𝐂𝐔𝐑𝐑𝐄𝐍𝐓 𝐒𝐓𝐀𝐓𝐔𝐒 ⟿ {status}

𝐑𝐀𝐍 𝐎𝐔𝐑 𝐎𝐅 𝐂𝐑𝐄𝐃𝐈𝐓? 𝗧𝘆𝗽𝗲 /buy
      """
            await message.reply_text(resp, message.id)
            plancheck = plan_expirychk(user_id)
            if plancheck == "YES":
                resp = """
𝐇𝐄𝐘 𝐁𝐎𝐙𝐎𝐎!
𝐏𝐋𝐀𝐍 𝐄𝐗𝐏𝐈𝐑𝐄𝐃 𝐁𝐀𝐁𝐘! 𝐁𝐔𝐘 /buy 𝐨𝐫 𝐁𝐄𝐆 @stripe_xD
        """
                await Client.send_message(user_id, resp)
            else:
                pass
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")
