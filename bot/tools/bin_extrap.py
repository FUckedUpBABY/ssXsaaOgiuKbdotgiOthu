from pyrogram import Client, filters
from FUNC.usersdb_func import *
from FUNC.defs import *
import random


@Client.on_message(filters.command("bxt", [".", "/"]))
async def cmd_bin(Client, message):
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
            checkgroup = str(getchatinfo(chat_id))
            if chat_type == "ChatType.PRIVATE" and status == "FREE":
                resp = "𝐔𝐍𝐀𝐔𝐓𝐇𝐎𝐑𝐈𝐙𝐄𝐃 𝐔𝐒𝐄𝐑"
                await message.reply_text(resp, message.id)

            elif chat_type == "ChatType.GROUP" or chat_type == "ChatType.SUPERGROUP" and checkgroup == "None":
                resp = "𝐂𝐇𝐀𝐓 𝐈𝐒 𝐍𝐎𝐓 𝐀𝐔𝐓𝐇𝐎𝐑𝐈𝐙𝐄𝐃 𝐓𝐎 𝐔𝐒𝐄 𝐓𝐇𝐈𝐒 𝐂𝐎𝐌𝐌𝐀𝐍𝐃, 𝐀𝐒𝐊 𝐌𝐘 𝐎𝐖𝐍𝐄𝐑 @stripe_xD "
                await message.reply_text(resp, message.id)
            else:
                msg = message.text.split(" ")
                try:
                    try:
                        cc = msg[1]
                    except:
                        cc = message.reply_to_message.text
                except Exception as e:
                    resp = "𝗚𝗜𝗩𝗘 𝗔 𝗩𝗔𝗟𝗜𝗗 𝗕𝗜𝗡 ❌"
                    await message.reply_text(resp, message.id)
                bin = cc[:6]
                bin_ex = f"{bin}{cc_extrap()}xxxx"
                bin_mes = f"0{random.randint(1,9)}"
                bin_ano = f"{random.randint(22,35)}"
                full_extrap = f"{bin_ex}|{bin_mes}|{bin_ano}|xxx"
                resp = f"""
𝐁𝐈𝐍 𝐄𝐗𝐓𝐑𝐀𝐏𝐄 𝐆𝐄𝐍𝐄𝐑𝐀𝐓𝐄𝐃 ✅ 

𝐁𝐈𝐍 𝐄𝐗𝐓𝐑𝐀𝐏𝐄 <code>{full_extrap}</code>  
𝗕𝗜𝗡 ⟿{bin}
𝗖𝗿𝗲𝗮𝘁𝗲𝗱 𝗕𝘆 <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ]
𝗧𝗼𝗼𝗸 0 𝘀𝗲𝗰𝗼𝗻𝗱𝘀 
𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 𝐂𝐇𝐄𝐂𝐊𝐄𝐑 𝐁𝐎𝐓 𝐎𝐅 𝐓𝐄𝐀𝐌 𝐍𝐌𝐁
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
