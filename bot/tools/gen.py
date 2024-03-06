from pyrogram import Client, filters
from pathlib import Path
import requests
import json
import re
import time
from FUNC.usersdb_func import *
from FUNC.cc_gen import *
import requests
import json

session = requests.session()


@Client.on_message(filters.command("gen", [".", "/"]))
async def cmd_gen(Client, message):
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

                if message.reply_to_message:
                    bin = message.reply_to_message.text

                else:
                    msg = message.text.split(" ")
                    try:
                        gen_msg = msg[1]
                    except:
                        gen_msg = ""
                    if len(gen_msg) == 0:
                        resp = f"""<b>
𝐅𝐎𝐑𝐌𝐀𝐓 𝐈𝐍𝐕𝐀𝐋𝐈𝐃

𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒:
Only Bin
<code>/gen 447697</code>

Bin With Expiration
<code>/gen 447697|12</code>
<code>/gen 447697|12|23</code>

Bin With Fixed CVV
<code>/gen 447697|12|23|000</code>

Bin With Custom Amount
<code>/gen 447697 100</code>
            </b>"""
                        await message.reply_text(resp, message.id)
                    else:
                        gen_cc = gen_msg.split("|")
                        try:
                            cc = gen_cc[0]
                            list = re.findall(r"[0-9]+", cc)
                            cc = list[0]
                        except:
                            cc = "x"
                        try:
                            mes = gen_cc[1]
                        except:
                            mes = "x"
                        try:
                            ano = gen_cc[2]
                        except:
                            ano = "x"
                        try:
                            cvv = gen_cc[3]
                        except:
                            cvv = "x"
                        if len(gen_cc) == 1 and len(gen_msg) > 5:
                            list = re.findall(r"[0-9]+", gen_msg)
                            gen_msg = list[0]
                            total = [f"{gen_msg}", f"x", f"x", f"x"]
                        elif len(gen_cc) == 2 and len(cc) > 5:
                            total = [f"{cc}", f"{mes}", f"x", f"x"]
                        elif len(gen_cc) == 3 and len(cc) > 5:
                            total = [f"{cc}", f"{mes}", f"{ano}", f"x"]
                        elif len(gen_cc) == 4 and len(cc) > 5:
                            total = [f"{cc}", f"{mes}", f"{ano}", f"{cvv}"]
                        else:
                            total = "N/A"
                        if total == "N/A":
                            resp = f"""
𝐅𝐎𝐑𝐌𝐀𝐓 𝐈𝐍𝐕𝐀𝐋𝐈𝐃

𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒:
Only Bin
<code>/gen 447697</code>

Bin With Expiration
<code>/gen 447697|12</code>
<code>/gen 447697|12|23</code>

Bin With Fixed CVV
<code>/gen 447697|12|23|000</code>

Bin With Custom Amount
<code>/gen 447697 100</code>
              """
                            await message.reply_text(resp, message.id)
                        else:
                            delete = await message.reply_text(
                                "𝗚𝗲𝗻𝗮𝗿𝗮𝘁𝗶𝗻𝗴...", message.id)
                            tic = time.perf_counter()
                            fr_cc = total[0]
                            fr_mes = total[1]
                            fr_ano = total[2]
                            fr_cvv = total[3]
                            format = f"{fr_cc}|{fr_mes}|{fr_ano}|{fr_cvv}"
                            allcc = ""
                            try:
                                amt = int(msg[2])
                            except:
                                amt = 15
                            if amt == 15:
                                for i in range(15):
                                    gennned = luhnccgen(total)
                                    allcc += f"{gennned}\n"
                                toc = time.perf_counter()
                                resp = f"""
𝐂𝐑𝐄𝐃𝐈𝐓 𝐂𝐀𝐑𝐃 𝐆𝐄𝐍𝐄𝐑𝐀𝐓𝐄𝐃 ✅
𝗔𝗠𝗢𝗨𝗡𝗧: <b>15</b>
𝗔𝗹𝗴𝗼𝗿𝗶𝘁𝗵𝗺: NEW ALGORITHM
𝗕𝗜𝗡: <b>{format}</b>

<code>{allcc}</code>

𝗚𝗲𝗻𝗻𝗲𝗱 𝗕𝘆 <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ]
𝗧𝗶𝗺𝗲 𝗧𝗮𝗸𝗲𝗻: <b>{toc - tic:0.4f}𝘀</b>
𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 𝐂𝐇𝐄𝐂𝐊𝐄𝐑 𝐁𝐎𝐓 𝐎𝐅 𝐓𝐄𝐀𝐌 𝐍𝐌𝐁
                """
                                await Client.delete_messages(
                                    message.chat.id, delete.id)
                                await message.reply_text(resp, message.id)
                            elif amt > 100000:
                                resp = "𝐁𝐎𝐙𝐎 𝐍𝐄𝐄𝐃 𝟏𝟎𝟎𝐊+ 𝐂𝐂? 𝐈𝐃𝐈𝐎𝐓 𝐋𝐎𝐖𝐄𝐑 𝐓𝐇𝐄 𝐀𝐌𝐎𝐔𝐍𝐓 𝐔𝐍𝐃𝐄𝐑 𝟏𝟎𝟎𝐊"
                                await message.reply_text(resp, message.id)
                            else:
                                filename = f"{amt}X_CC_GENARATED_BY_{user_id}.txt"
                                for i in range(amt):
                                    gennned = luhnccgen(total)
                                    with open(filename, "a") as f:
                                        f.write(f"{gennned}\n")
                                toc = time.perf_counter()
                                caption = f"""
𝐂𝐑𝐄𝐃𝐈𝐓 𝐂𝐀𝐑𝐃 𝐆𝐄𝐍𝐄𝐑𝐀𝐓𝐄𝐃 ✅

𝗔𝗠𝗢𝗨𝗡𝗧: <b>{amt}</b>
𝗔𝗹𝗴𝗼𝗿𝗶𝘁𝗵𝗺: NEW ALGORITHM
𝗕𝗜𝗡: <b>{format}</b>
𝗚𝗲𝗻𝗻𝗲𝗱 𝗕𝘆 <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ]
𝗧𝗶𝗺𝗲 𝗧𝗮𝗸𝗲𝗻: <b>{toc - tic:0.4f}𝘀</b>
𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 𝐂𝐇𝐄𝐂𝐊𝐄𝐑 𝐁𝐎𝐓 𝐎𝐅 𝐓𝐄𝐀𝐌 𝐍𝐌𝐁"""
                                await Client.delete_messages(
                                    message.chat.id, delete.id)
                                scr_done = await message.reply_document(
                                    document=filename,
                                    caption=caption,
                                    reply_to_message_id=message.id)
                                if scr_done:
                                    name = filename
                                    my_file = Path(name)
                                    my_file.unlink(missing_ok=True)
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
