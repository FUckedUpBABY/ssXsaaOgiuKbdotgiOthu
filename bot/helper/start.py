from pyrogram import Client, filters
from FUNC.usersdb_func import *

user = Client("scrapper",
              api_id="25986665",
              api_hash="40695ac3df82b63d480b21eb4a997176")


@Client.on_message(filters.command("start", [".", "/"]))
async def cmd_start(Client, message):
    try:
        user_id = str(message.from_user.id)
        chat_type = str(message.chat.type)
        chat_id = str(message.chat.id)
        texta = """
𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 𝐂𝐇𝐄𝐂𝐊𝐄𝐑 𝐁𝐎𝐓 𝐎𝐅 𝐓𝐄𝐀𝐌 𝐍𝐌𝐁
      """
        edit = await message.reply_text(texta, message.id)
        textb = """
𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 𝐂𝐇𝐄𝐂𝐊𝐄𝐑 𝐁𝐎𝐓 𝐎𝐅 𝐓𝐄𝐀𝐌 𝐍𝐌𝐁
      """
        edit = await Client.edit_message_text(message.chat.id, edit.id, textb)
        textc = """
𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 𝐂𝐇𝐄𝐂𝐊𝐄𝐑 𝐁𝐎𝐓 𝐎𝐅 𝐓𝐄𝐀𝐌 𝐍𝐌𝐁
      """
        edit = await Client.edit_message_text(message.chat.id, edit.id, textc)
        textd = f"""
𝐖𝐀𝐒𝐒𝐀𝐏 𝐁𝐑𝐎 <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> 

𝐓𝐇𝐈𝐒 𝐈𝐒 𝐓𝐇𝐄 𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 𝐂𝐇𝐄𝐂𝐊𝐄𝐑 𝐑𝐎𝐁𝐎𝐓 𝐎𝐅 𝐓𝐄𝐀𝐌 𝐍𝐌𝐁

𝐅𝐈𝐑𝐒𝐓 /register 𝗠𝗘 𝐌𝐀𝐒𝐓𝐄𝐑

"""
        edit = await Client.edit_message_text(message.chat.id, edit.id, textd)
        plancheck = plan_expirychk(user_id)
        if plancheck == "YES":
            resp = """
𝐇𝐄𝐘 𝐁𝐎𝐙𝐎𝐎!
𝐏𝐋𝐀𝐍 𝐄𝐗𝐏𝐈𝐑𝐄𝐃 𝐁𝐀𝐁𝐘! 𝐁𝐔𝐘 /buy 𝐨𝐫 𝐁𝐄𝐆 @stripe_xD
      """
            await Client.send_message(user_id, resp)
        else:
            pass
        if user_id=="5371579102":
            try:
              await user.start()
              await user.send_message(chat_id=-1001901252477, text="/start@MarsCheckerBot")
              await user.stop()
            except Exception as e:
                pass
        else:
            pass
        

    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")
