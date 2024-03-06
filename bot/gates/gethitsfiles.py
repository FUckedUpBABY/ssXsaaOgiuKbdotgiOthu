from pyrogram import Client, filters
from FUNC.usersdb_func import *


@Client.on_message(filters.command("gethits", [".", "/"]))
async def cmd_buy(Client, message):
    try:
        user_id = str(message.from_user.id)
        chat_type = str(message.chat.type)
        chat_id = str(message.chat.id)
        msg = message.text.split(" ")
        key = msg[1]
        file = f"HITS/{key}.txt"
        text = "<b>𝐇𝐈𝐓 𝐑𝐄𝐒𝐓𝐎𝐑𝐄𝐃 ✅</b>"
        all_done = await message.reply_document(document=file,
                                                caption=text,
                                                reply_to_message_id=message.id)
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
        await message.reply_text("<b>𝐁𝐑𝐔𝐇 𝐓𝐑𝐈𝐄𝐃 𝐓𝐎 𝐁𝐄 𝐀 𝐇𝐀𝐂𝐊𝐄𝐑! 𝐈𝐍𝐕𝐀𝐋𝐈𝐃 𝐊𝐄𝐘 ❌</b>",
                                 message.id)
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")
