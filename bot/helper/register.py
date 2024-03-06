from pyrogram import Client, filters
import time
from datetime import date
from datetime import timedelta
from FUNC.usersdb_func import *
import pymongo
from mongodb import *


@Client.on_message(filters.command("register", [".", "/"]))
async def cmd_register(Client, message):
    try:
        user_id = str(message.from_user.id)
        username = str(message.from_user.username)
        chat_id = str(message.chat.id)
        antispam_time = int(time.time())
        tt = str(date.today())
        split = tt.split("-")
        yy = split[0]
        mm = split[1]
        dd = split[2]
        reg_at = f"{dd}-{mm}-{yy}"
        find = usersdb.find_one({"id": f"{user_id}"}, {"_id": 0})
        registration_check = str(find)
        if registration_check == "None":
            info = {
                "id": f"{user_id}",
                "username": f"{username}",
                "status": f"FREE",
                "plan": f"N/A",
                "expiry": "N/A",
                "credit": "100",
                "antispam_time": f"{antispam_time}",
                "totalkey": "0",
                "reg_at": f"{reg_at}"
            }
            insert = usersdb.insert_one(info)
            resp = "𝐑𝐄𝐆𝐈𝐒𝐓𝐑𝐀𝐓𝐈𝐎𝐍 𝐒𝐔𝐂𝐊𝐒𝐄𝐗𝐅𝐔𝐋𝐋 𝐃𝐄𝐀𝐑! ✅ 𝐂𝐌𝐃 ⟿ /cmds 𝐓𝐎 𝐊𝐍𝐎𝐖 𝐌𝐘 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒"
        else:
            resp = "𝐘𝐎𝐔 𝐀𝐑𝐄 𝐀𝐋𝐑𝐄𝐀𝐃𝐘 𝐀 𝐒𝐔𝐏𝐄𝐑𝐌𝐀𝐍! ✅ 𝐂𝐌𝐃 ⟿ /cmds 𝐓𝐎 𝐊𝐍𝐎𝐖 𝐌𝐘 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒"

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
