from pyrogram import Client, filters
from FUNC.usersdb_func import *
import random


@Client.on_message(filters.command("gay", [".", "/"]))
async def cmd_id(Client, message):
    try:
        user_id = str(message.from_user.id)
        if user_id == "5371579102":
            gayness = "0"
        else:
            gayness = random.randint(0, 100)
        #PLAN CHECK
        if message.reply_to_message:
            user_id = str(message.reply_to_message.from_user.id)
            if user_id == "5371579102":
                gayness = "0"
            else:
                gayness = random.randint(0, 100)
            texta = f"""
𝐖𝐀𝐒𝐒𝐀𝐏 𝐁𝐑𝐎 <a href="tg://user?id={message.reply_to_message.from_user.id}"> {message.reply_to_message.from_user.first_name}</a> !

𝐁𝐑𝐔𝐇! 𝐑𝐔𝐍! 𝐘𝐎𝐔 𝐀𝐑𝐄 <b>{gayness}%</b> 𝐆𝐀𝐘! 𝐖𝐓𝐅 𝐁𝐎𝐙𝐎 😂🤐
    """
            msg1 = await message.reply_text(texta, message.id)
        else:
            texta = f"""
𝐖𝐀𝐒𝐒𝐀𝐏 𝐁𝐑𝐎 <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> !

𝐁𝐑𝐔𝐇! 𝐑𝐔𝐍! 𝐘𝐎𝐔 𝐀𝐑𝐄 <b>{gayness}%</b> 𝐆𝐀𝐘! 𝐖𝐓𝐅 𝐁𝐎𝐙𝐎 😂🤐
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
