from pyrogram import Client, filters
from FUNC.usersdb_func import *


@Client.on_message(filters.command("id", [".", "/"]))
async def cmd_id(Client, message):
    try:
        user_id = str(message.from_user.id)
        chat_type = str(message.chat.type)
        chat_id = str(message.chat.id)
        #PLAN CHECK
        if message.reply_to_message:
            texta = f"""
𝐖𝐀𝐒𝐒𝐀𝐏 𝐁𝐑𝐎 <a href="tg://user?id={message.reply_to_message.from_user.id}"> {message.reply_to_message.from_user.first_name}</a> !
𝐘𝐎𝐔𝐑 𝐏𝐄𝐑𝐌𝐀𝐍𝐄𝐍𝐓 𝐔𝐒𝐄𝐑 𝐈𝐃 ⟿ <code>{message.reply_to_message.from_user.id}</code> 
𝐂𝐇𝐀𝐓 𝐈𝐃 ⟿ <code>{message.chat.id}</code>
"""
            msg1 = await message.reply_text(texta, message.id)
        else:
            texta = f"""
𝐖𝐀𝐒𝐒𝐀𝐏 𝐁𝐑𝐎 <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> !
𝐘𝐎𝐔𝐑 𝐏𝐄𝐑𝐌𝐀𝐍𝐄𝐍𝐓 𝐔𝐒𝐄𝐑 𝐈𝐃 ⟿ <code>{message.from_user.id}</code> 
𝐂𝐇𝐀𝐓 𝐈𝐃 ⟿ <code>{message.chat.id}</code>
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
