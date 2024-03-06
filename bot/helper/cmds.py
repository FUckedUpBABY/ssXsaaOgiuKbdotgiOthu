from pyrogram import Client, filters
from FUNC.usersdb_func import *


@Client.on_message(filters.command("cmds", [".", "/"]))
async def cmd_cmds(Client, message):
    try:
        user_id = str(message.from_user.id)
        chat_type = str(message.chat.type)
        chat_id = str(message.chat.id)
        regdata = str(getuserinfo(user_id))
        if regdata == 'None':
            resp = "𝐔𝐧𝐫𝐞𝐠𝐢𝐬𝐭𝐞𝐫𝐞𝐝 𝐔𝐬𝐞𝐫. 𝐏𝐫𝐞𝐬𝐬 /register 𝐭𝐨 𝐮𝐬𝐞 𝐦𝐞."
            await message.reply_text(resp, message.id)
        else:
            user_id = str(message.from_user.id)
            chat_type = str(message.chat.type)
            chat_id = str(message.chat.id)
            texta = f"""
  𝐖𝐀𝐒𝐒𝐀𝐏 𝐁𝐑𝐎 <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
  𝗟𝗼𝗮𝗱𝗶𝗻𝗴 𝗮𝗹𝗹 𝗼𝗳 𝗫𝗖𝗖 𝗕𝗢𝗧 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀..
      """
            msg1 = await message.reply_text(texta, message.id)
            textb = """
- 𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 𝐂𝐇𝐄𝐂𝐊𝐄𝐑 𝐁𝐎𝐓 𝐎𝐅 𝐓𝐄𝐀𝐌 𝐍𝐌𝐁 𝗔𝗟𝗟 𝐂𝐌𝐃𝐒

∎ 🔥 𝐆𝐀𝐓𝐄 𝐈𝐍𝐅𝐎 ⇝ 𝐓𝐎 𝐂𝐇𝐄𝐂𝐊 𝐓𝐇𝐄 𝐆𝐀𝐓𝐄𝐖𝐀𝐘𝐒 𝐎𝐅 𝐘𝐎𝐔𝐑 𝐅𝐀𝐕𝐎𝐔𝐑𝐈𝐓𝐄 𝐒𝐈𝐓𝐄𝐒 
<code>/gate https://follovery.com</code>

∎ 🔥 𝐆𝐀𝐓𝐄𝐖𝐀𝐘 𝐕𝟐 ⇝ 𝐀𝐃𝐕𝐀𝐍𝐂𝐄𝐃 𝐆𝐀𝐓𝐄𝐖𝐀𝐘 𝐅𝐈𝐍𝐃𝐄𝐑 𝐕𝟐
<code>/url https://follovery.com</code>

∎ 🔥 𝐓𝐎𝐎𝐋𝐒 ⇝ 𝐒𝐊 𝐈𝐍𝐅𝐎 𝐂𝐇𝐄𝐂𝐊
<code>/sk sk_live_51kvhhbrfFJrdfTg</code>

∎ 𝐆𝐀𝐓𝐄 ⇝ 𝐒𝐓𝐑𝐈𝐏𝐄 𝐀𝐔𝐓𝐇
<code>/au cc|mm|yy|cvv</code>

∎ 𝐆𝐀𝐓𝐄 ⇝ 𝐀𝐃𝐘𝐄𝐍 𝐀𝐔𝐓𝐇
<code>/aD cc|mm|yy|cvv</code>

∎ 𝐆𝐀𝐓𝐄 ⇝ 𝐒𝐓𝐑𝐈𝐏𝐄 𝐂𝐇𝐀𝐑𝐆𝐄 𝟎.𝟓$
<code>/chk cc|mm|yy|cvv</code>

∎ 𝐆𝐀𝐓𝐄 ⇝ 𝐒𝐇𝐎𝐏𝐈𝐅𝐘 𝐂𝐇𝐀𝐑𝐆𝐄
<code>/sh cc|mm|yy|cvv</code>

∎ 𝐆𝐀𝐓𝐄 ⇝ 𝐌𝐀𝐒𝐒 𝐀𝐔𝐓𝐇 𝐒𝐓𝐑𝐈𝐏𝐄
<code>/mass cc|mm|yy|cvv</code>

∎ 𝐆𝐀𝐓𝐄 ⇝ 𝐌𝐀𝐒𝐒 𝐂𝐇𝐀𝐑𝐆𝐄 𝐒𝐓𝐑𝐈𝐏𝐄 𝟎.𝟓$
<code>/mchk cc|mm|yy|cvv</code>

∎ 𝐆𝐀𝐓𝐄 ⇝ 𝐌𝐀𝐒𝐒 𝐀𝐔𝐓𝐇 𝐒𝐓𝐑𝐈𝐏𝐄 (𝐑𝐄𝐏𝐋𝐘 𝐓𝐎 𝐓𝐗𝐓)
<code>/masstxt</code>

∎ 𝐆𝐀𝐓𝐄 ⇝ 𝐌𝐀𝐒𝐒 𝐂𝐇𝐀𝐑𝐆𝐄 𝐒𝐓𝐑𝐈𝐏𝐄 𝟎.𝟓$ (𝐑𝐄𝐏𝐋𝐘 𝐓𝐎 𝐓𝐗𝐓)
<code>/mchktxt</code>

∎ 𝐆𝐀𝐓𝐄 ⇝ 𝐂𝐂𝐍 𝐂𝐇𝐀𝐑𝐆𝐄 𝟎.𝟓$
<code>/ccn</code>

∎ 𝐆𝐀𝐓𝐄 ⇝ 𝐌𝐀𝐒𝐒 𝐂𝐂𝐍 𝐂𝐇𝐀𝐑𝐆𝐄 𝟎.𝟓$
<code>/mccn</code>

∎ 𝐆𝐀𝐓𝐄 ⇝ 𝐌𝐀𝐒𝐒 𝐂𝐂𝐍 𝐂𝐇𝐀𝐑𝐆𝐄 𝟎.𝟓$ (𝐑𝐄𝐏𝐋𝐘 𝐓𝐎 𝐓𝐗𝐓)
<code>/mccntxt</code>

∎ 𝐆𝐀𝐓𝐄 ⇝ 𝐌𝐀𝐒𝐒 𝐒𝐇𝐎𝐏𝐈𝐅𝐘 𝐂𝐇𝐀𝐑𝐆𝐄
<code>/mchksh cc|mm|yy|cvv</code>

∎ 𝐓𝐎𝐎𝐋𝐒 ⇝ 𝐆𝐄𝐓 𝐇𝐈𝐓𝐒
<code>/gethits secretkey</code>

∎ 𝐓𝐎𝐎𝐋𝐒 ⇝ 𝐂𝐑𝐄𝐃𝐈𝐓 𝐂𝐀𝐑𝐃 𝐒𝐂𝐑𝐀𝐏𝐏𝐄𝐑
<code>/scr liveccbycp 100</code>

∎ 𝐓𝐎𝐎𝐋𝐒 ⇝ 𝐂𝐑𝐄𝐃𝐈𝐓 𝐂𝐀𝐑𝐃 𝐈𝐍𝐅𝐎 𝐂𝐇𝐄𝐂𝐊
<code>/bin cc|mm|yy|cvv</code>

∎ 𝐓𝐎𝐎𝐋𝐒 ⇝ 𝐂𝐀𝐑𝐃𝐬 𝐄𝐗𝐓𝐑𝐀𝐏 𝐌𝐀𝐊𝐄𝐑
<code>/cxt cc|mm|yy|cvv</code>

∎ 𝐓𝐎𝐎𝐋𝐒 ⇝ 𝐁𝐈𝐍𝐬 𝐄𝐗𝐓𝐑𝐀𝐏 𝐌𝐀𝐊𝐄𝐑
<code>/bxt cc|mm|yy|cvv</code>

∎ 𝐓𝐎𝐎𝐋𝐒 ⇝ 𝐂𝐀𝐑𝐃 𝐆𝐄𝐍𝐄𝐑𝐀𝐓𝐎𝐑
<code>/gen bin</code>

∎ 𝐈𝐍𝐅𝐎⇝ 𝐔𝐒𝐄𝐑 𝐈𝐃 𝐀𝐍𝐃 𝐒𝐓𝐀𝐓𝐔𝐒
<code>/id</code>

∎ 𝐈𝐍𝐅𝐎⇝ 𝐔𝐒𝐄𝐑 𝐈𝐍𝐅𝐎𝐑𝐌𝐀𝐓𝐈𝐎𝐍 𝐀𝐍𝐃 𝐒𝐓𝐀𝐓𝐔𝐒
<code>/info</code>

∎ 𝐈𝐍𝐅𝐎⇝ 𝐂𝐑𝐄𝐃𝐈𝐓 𝐈𝐍𝐅𝐎𝐑𝐌𝐀𝐓𝐈𝐎𝐍
<code>/credits</code>

∎ 𝐒𝐓𝐀𝐑𝐓⇝ 𝐑𝐄𝐆𝐈𝐒𝐓𝐑𝐀𝐓𝐈𝐎𝐍
<code>/register</code>

∎ 𝐀𝐔𝐓𝐇⇝ 𝐓𝐎 𝐀𝐃𝐃 𝐓𝐇𝐈𝐒 𝐁𝐎𝐓 𝐈𝐍𝐓𝐎 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏
<code>/howgp</code>

∎ 𝐅𝐔𝐍⇝ 𝐂𝐇𝐄𝐂𝐊 𝐀𝐑𝐄 𝐀 𝐆𝐀𝐘 𝐎𝐑 𝐖𝐇𝐀𝐓!
<code>/gay</code>

∎ 𝐁𝐔𝐘⇝ 𝐓𝐎 𝐁𝐔𝐘 𝐁𝐎𝐓 𝐏𝐋𝐀𝐍𝐒
<code>/buy</code>


𝐀𝐓𝐓𝐄𝐍𝐓𝐈𝐎𝐍 ⇝ 𝐓𝐇𝐈𝐒 𝐈𝐒 𝐀 𝐁𝐄𝐓𝐀 𝐓𝐄𝐒𝐓𝐈𝐍𝐆 𝐁𝐎𝐓 𝐏𝐑𝐄𝐕𝐈𝐄𝐖. 𝐖𝐀𝐈𝐓 𝐅𝐎𝐑 𝐓𝐇𝐄 𝐅𝐈𝐍𝐀𝐋 𝐑𝐄𝐒𝐔𝐋𝐓 𝐅𝐎𝐑 𝐒𝐀𝐓𝐈𝐒𝐅𝐀𝐂𝐓𝐎𝐑𝐘 𝐑𝐄𝐒𝐔𝐋𝐓𝐒.
      """
            msg2 = await Client.edit_message_text(message.chat.id, msg1.id,
                                                  textb)
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
