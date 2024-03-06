from pyrogram import Client, filters
import json
import re
import time
from FUNC.usersdb_func import *
import concurrent.futures
from FUNC.defs import *
from FUNC.skfunc import *
import threading
import asyncio


@Client.on_message(filters.command("skmass", [".", "/"]))
def multi(Client, message):
    t1 = threading.Thread(target=bcall, args=(Client, message))
    t1.start()


def bcall(Client, message):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(thread(Client, message))
    loop.close()


async def thread(Client, message):
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
                if credit < 3:
                    resp = "𝐒𝐎𝐑𝐑𝐘 𝐁𝐑𝐎! 𝐑𝐀𝐍 𝐎𝐔𝐓 𝐎𝐅 𝐂𝐑𝐄𝐃𝐈𝐓𝐒 𝐋𝐌𝐀𝐎. 𝐓𝐎 𝐁𝐔𝐘 𝐃𝐦 @stripe_xD"
                    await message.reply_text(resp, message.id)
                else:
                    now = int(time.time())
                    count_antispam = now - antispam_time
                    if count_antispam < 15 and role == 'FREE':
                        after = 15 - count_antispam
                        resp = f"""
𝐒𝐏𝐀𝐌𝐌𝐄𝐑 𝐒𝐓𝐅𝐔!
𝐃𝐎𝐍'𝐓 𝐓𝐑𝐘 𝐁𝐄𝐅𝐎𝐑𝐄 {after} 𝗦𝗘𝗖𝗢𝗡𝗗𝗦
            """
                        await message.reply_text(resp, message.id)
                    elif count_antispam < 10 and role == 'PREMIUM':
                        after = 10 - count_antispam
                        resp = f"""
𝐒𝐏𝐀𝐌𝐌𝐄𝐑 𝐒𝐓𝐅𝐔!
𝐃𝐎𝐍'𝐓 𝐓𝐑𝐘 𝐁𝐄𝐅𝐎𝐑𝐄 {after} 𝗦𝗘𝗖𝗢𝗡𝗗𝗦
            """
                        await message.reply_text(resp, message.id)
                    elif count_antispam < 5 and role == '𝐏𝐞𝐫𝐦𝐚𝐧𝐞𝐧𝐭':
                        after = 5 - count_antispam
                        resp = f"""
𝐒𝐏𝐀𝐌𝐌𝐄𝐑 𝐒𝐓𝐅𝐔!
𝐃𝐎𝐍'𝐓 𝐓𝐑𝐘 𝐁𝐄𝐅𝐎𝐑𝐄 {after} 𝗦𝗘𝗖𝗢𝗡𝗗𝗦
            """
                        await message.reply_text(resp, message.id)
                    else:
                        all_cards = message.text.split('\n')
                        stresp = "𝗦𝗧𝗔𝗥𝗧𝗘𝗗 𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚.."
                        stchk = await message.reply_text(stresp, message.id)
                        len_cards = len(all_cards)
                        if len(all_cards) > 9 and role == "FREE":
                            resp = "𝗦𝗢𝗥𝗥𝗬 𝐅𝐫𝐞𝐞 𝐁𝐨𝐳𝐨𝐬 𝐚𝐫𝐞 𝐋𝐢𝐦𝐢𝐭𝐞𝐝 𝐭𝐨 8 𝐒𝐊❌"
                            free = await Client.edit_message_text(
                                message.chat.id, stchk.id, resp)
                        elif len(all_cards) > 16 and role == 'PREMIUM':
                            resp = "𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐁𝐎𝐙𝐎𝐒 𝐂𝐀𝐍 𝐂𝐇𝐄𝐂𝐊 𝐔𝐏𝐓𝐎 15 𝐒𝐊❌"
                            PREMIUM = await Client.edit_message_text(
                                message.chat.id, stchk.id, resp)
                        elif len(all_cards) > 26 and role == '𝐏𝐞𝐫𝐦𝐚𝐧𝐞𝐧𝐭':
                            resp = "𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐁𝐎𝐙𝐎𝐒 𝐂𝐀𝐍 𝐂𝐇𝐄𝐂𝐊 𝐔𝐏𝐓𝐎 25 𝐒𝐊❌"
                            PREMIUM = await Client.edit_message_text(
                                message.chat.id, stchk.id, resp)
                        else:
                            resp = "𝐑𝐄𝐒𝐔𝐋𝐓 ⟿ 𝐖𝐀𝐈𝐓 𝐏𝐋𝐄𝐀𝐒𝐄! 𝐆𝐄𝐓𝐓𝐈𝐍𝐆 𝐈𝐍𝐏𝐔𝐓𝐒"
                            okst = await Client.edit_message_text(
                                message.chat.id, stchk.id, resp)
                            cards = []
                            for x in all_cards:
                                if "skmass" in x:
                                    x = x.split("skmass ")[1]
                                    cards.append(x)
                                else:
                                    cards.append(x)

                            len_cards = len(cards)
                            if not len_cards:
                                resp = "𝐑𝐄𝐒𝐔𝐋𝐓 ⟿ 𝐅𝐎𝐔𝐍𝐃 𝐍𝐎 𝐕𝐀𝐋𝐈𝐃 𝐂𝐂"
                                nov = await Client.edit_message_text(
                                    message.chat.id, okst.id, resp)
                            else:
                                resp = f"𝐑𝐄𝐒𝐔𝐋𝐓 ⟿ 𝐂𝐂 𝐅𝐄𝐓𝐂𝐇𝐄𝐃 {len_cards} 𝐓𝐇𝐈𝐒 𝐀𝐌𝐎𝐔𝐍𝐓. 𝐊𝐈𝐍𝐃𝐋𝐘 𝐖𝐀𝐈𝐓 𝐔𝐍𝐓𝐈𝐋 𝐂𝐇𝐄𝐂𝐊 𝐅𝐈𝐍𝐈𝐒𝐇𝐄𝐃"
                                nov = await Client.edit_message_text(
                                    message.chat.id, okst.id, resp)

                                text = f"""
<b>𝐆𝐀𝐓𝐄 ⟿ 𝐌𝐀𝐒𝐒 𝐒𝐊 𝐂𝐇𝐄𝐂𝐊</b> \n
"""
                                amt = 0
                                with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
                                    futures = []
                                    for i in cards:
                                        future = executor.submit(skmass,i)
                                        futures.append(future)
                                    for future in concurrent.futures.as_completed(futures):
                                        result = future.result()
                                        amt += 1
                                        calc = amt % 5
                                        text += result
                                        if calc==0:
                                            done = await Client.edit_message_text(
                                                message.chat.id, nov.id, text)
                                        else:
                                            pass
                                text += f"""
<b>

 
𝐑𝐄𝐒𝐔𝐋𝐓 ⟿ 𝐓𝐎𝐓𝐀𝐋 𝐒𝐊 𝐂𝐇𝐄𝐂𝐊 {len_cards}
𝐂𝐑𝐄𝐃𝐈𝐓 𝐒𝐏𝐄𝐍𝐓 ⟿ {len_cards}
𝐔𝐒𝐄𝐑 ⟿ <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> 🗿 [ {role}]
- 𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 𝐂𝐇𝐄𝐂𝐊𝐄𝐑 𝐁𝐎𝐓 𝐎𝐅 𝐓𝐄𝐀𝐌 𝐍𝐌𝐁
</b>
"""
                                await Client.edit_message_text(
                                    message.chat.id, nov.id, text)
                                #ANTISPAM TIME SET
                                massdeductcredit(user_id,len_cards)
                                setantispamtime(user_id)
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
