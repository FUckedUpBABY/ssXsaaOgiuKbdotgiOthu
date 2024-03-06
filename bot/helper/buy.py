from pyrogram import Client, filters
from FUNC.usersdb_func import *


@Client.on_message(filters.command("buy", [".", "/"]))
async def cmd_buy(Client, message):
    try:
        user_id = str(message.from_user.id)
        chat_type = str(message.chat.type)
        chat_id = str(message.chat.id)
        #PLAN CHECK
        resp = f"""
𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 𝐂𝐇𝐄𝐂𝐊𝐄𝐑 𝐁𝐎𝐓 𝐎𝐅 𝐓𝐄𝐀𝐌 𝐍𝐌𝐁 𝗣𝗹𝗮𝗻𝘀 :
⊶⊶⊶

𝟓𝟎𝟎𝟎 𝐂𝐫𝐞𝐝𝐢𝐭𝐬 + 𝟏 𝐝𝐚𝐲 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐚𝐜𝐜𝐞𝐬𝐬 - $𝟓
𝟐𝟎𝟎𝟎𝟎 𝐂𝐫𝐞𝐝𝐢𝐭𝐬 + 𝟑 𝐝𝐚𝐲𝐬 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐚𝐜𝐜𝐞𝐬𝐬 - $𝟏𝟓
𝟒𝟎𝟎𝟎𝟎 𝐂𝐫𝐞𝐝𝐢𝐭𝐬 + 𝟏 𝐰𝐞𝐞𝐤 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐚𝐜𝐜𝐞𝐬𝐬 - $𝟐𝟎
𝟏𝟎,𝟎𝟎𝟎𝟎 𝐂𝐫𝐞𝐝𝐢𝐭𝐬 + 𝟏 𝐦𝐨𝐧𝐭𝐡 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐚𝐜𝐜𝐞𝐬𝐬 - $𝟑𝟎
𝟏𝟎𝟎𝟎𝟎 𝐂𝐫𝐞𝐝𝐢𝐭𝐬 $𝟓
𝟑𝟎𝟎𝟎𝟎 𝐂𝐫𝐞𝐝𝐢𝐭𝐬 $𝟏𝟎
𝟓𝟎𝟎𝟎𝟎 𝐂𝐫𝐞𝐝𝐢𝐭𝐬 $𝟏𝟓
𝟏𝟎,𝟎𝟎𝟎𝟎 𝐂𝐫𝐞𝐝𝐢𝐭𝐬 $𝟐𝟎

𝘛𝘖 𝘉𝘜𝘠= 𝘋𝘔 @stripe_xD
    """
        msg1 = await message.reply_text(resp, message.id)
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
