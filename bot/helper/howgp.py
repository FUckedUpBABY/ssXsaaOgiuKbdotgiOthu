from pyrogram import Client, filters
from FUNC.usersdb_func import *


@Client.on_message(filters.command("howgp", [".", "/"]))
async def cmd_howgp(Client, message):
    try:
        user_id = str(message.from_user.id)
        chat_type = str(message.chat.type)
        chat_id = str(message.chat.id)
        #PLAN CHECK

        texta = f"""
𝐀𝐃𝐃𝐈𝐍𝐆 𝐁𝐎𝐓 𝐈𝐍 𝐆𝐑𝐎𝐔𝐏 𝐂𝐔𝐑𝐑𝐄𝐍𝐓𝐋𝐘 𝐎𝐅𝐅

KINDLY <b>DO NOT DISTURB</b>

THANK YOU, JOIN @NOMOREBINS
"""
        msg1 = await message.reply_text(texta, message.id)
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
