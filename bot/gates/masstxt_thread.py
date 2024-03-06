from pyrogram import Client, filters
import json
import re
import time
from FUNC.usersdb_func import *
from FUNC.GATES.masstxtfunc import *
from FUNC.gc_func import *
import concurrent.futures
import threading
import asyncio
from pathlib import Path
import concurrent.futures


@Client.on_message(filters.command("masstxt", [".", "/"]))
def multi(Client, message):
    t1 = threading.Thread(target=bcall, args=(Client, message))
    t1.start()


def bcall(Client, message):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(thread(Client, message))
    loop.close()


async def thread(Client, message):
    # try:
        user_id = str(message.from_user.id)
        chat_type = str(message.chat.type)
        chat_id = str(message.chat.id)
        regdata = str(getuserinfo(user_id))
        if regdata == 'None':
            resp = "𝗬𝗢𝗨 𝗔𝗥𝗘 𝗡𝗢𝗧 𝗥𝗘𝗚𝗜𝗦𝗧𝗘𝗥𝗘𝗗 𝗬𝗘𝗧 ⚠️. 𝗥𝗘𝗚𝗜𝗦𝗧𝗘𝗥 𝗙𝗜𝗥𝗦𝗧 𝗕𝗬 𝗨𝗦𝗜𝗡𝗚 /register 𝗧𝗢 𝗨𝗦𝗘 𝗠𝗘."
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
                resp = "𝗢𝗡𝗟𝗬 𝗣𝗥𝗘𝗠𝗜𝗨𝗠 𝗠𝗘𝗠𝗕𝗘𝗥𝗦 𝗔𝗥𝗘 𝗔𝗟𝗟𝗢𝗪𝗘𝗗 𝗧𝗢 𝗨𝗦𝗘 𝗕𝗢𝗧 𝗜𝗡 𝗣𝗘𝗥𝗦𝗢𝗡𝗔𝗟 ⚠️.𝗬𝗢𝗨 𝗖𝗔𝗡 𝗨𝗦𝗘 𝗙𝗥𝗘𝗘𝗟𝗬 𝗕𝗢𝗧 𝗛𝗘𝗥𝗘 @cyberpirateschats"
                await message.reply_text(resp, message.id)

            elif chat_type == "ChatType.GROUP" or chat_type == "ChatType.SUPERGROUP" and checkgroup == "None":
                resp = "𝗨𝗡𝗔𝗨𝗧𝗛𝗢𝗥𝗜𝗭𝗘𝗗 𝗖𝗛𝗔𝗧 ❌. 𝗖𝗢𝗡𝗧𝗔𝗖𝗧 @mtctechx 𝗧𝗢 𝗔𝗨𝗧𝗛𝗢𝗥𝗜𝗭𝗘."
                await message.reply_text(resp, message.id)
            else:
                if credit < 3:
                    resp = "𝗬𝗢𝗨 𝗛𝗔𝗩𝗘 𝗜𝗡𝗦𝗨𝗙𝗙𝗜𝗖𝗜𝗘𝗡𝗧 𝗖𝗥𝗘𝗗𝗜𝗧 𝗧𝗢 𝗨𝗦𝗘 𝗠𝗘 ⚠️ . 𝗥𝗘𝗖𝗛𝗔𝗥𝗚𝗘 𝗖𝗥𝗘𝗗𝗜𝗧 𝗨𝗦𝗜𝗡𝗚 /buy 𝗢𝗥 𝗪𝗔𝗜𝗧 𝗙𝗢𝗥 𝗙𝗥𝗘𝗘 𝗖𝗥𝗘𝗗𝗜𝗧 𝗨𝗦𝗜𝗡𝗚 𝗚𝗜𝗙𝗧𝗖𝗢𝗗𝗘 ."
                    await message.reply_text(resp, message.id)
                else:
                    now = int(time.time())
                    count_antispam = now - antispam_time
                    if count_antispam < 15 and role == 'FREE':
                        after = 15 - count_antispam
                        resp = f"""
𝗔𝗡𝗧𝗜𝗦𝗣𝗔𝗠 ⚠️
𝗧𝗥𝗬 𝗔𝗚𝗔𝗜𝗡 𝗔𝗙𝗧𝗘𝗥 {after} 𝗦𝗘𝗖𝗢𝗡𝗗𝗦
            """
                        await message.reply_text(resp, message.id)
                    elif count_antispam < 10 and role == 'PREMIUM':
                        after = 10 - count_antispam
                        resp = f"""
𝗔𝗡𝗧𝗜𝗦𝗣𝗔𝗠 ⚠️
𝗧𝗥𝗬 𝗔𝗚𝗔𝗜𝗡 𝗔𝗙𝗧𝗘𝗥 {after} 𝗦𝗘𝗖𝗢𝗡𝗗𝗦
            """
                        await message.reply_text(resp, message.id)
                    elif count_antispam < 5 and role == '♥ LIFETIME ♥':
                        after = 5 - count_antispam
                        resp = f"""
𝗔𝗡𝗧𝗜𝗦𝗣𝗔𝗠 ⚠️
𝗧𝗥𝗬 𝗔𝗚𝗔𝗜𝗡 𝗔𝗙𝗧𝗘𝗥 {after} 𝗦𝗘𝗖𝗢𝗡𝗗𝗦
            """
                        await message.reply_text(resp, message.id)
                    else:
                        try:
                            rnd = gcgenfunc(len=8)
                            key = f"masstxt_{message.from_user.id}_{rnd}"
                            file_name = f"{key}.txt"
                            await message.reply_to_message.download(
                                file_name=file_name)
                            getfile = "YES"
                        except Exception as e:
                            getfile = "NO"
                            e = str(e)
                            if e == "'NoneType' object has no attribute 'download'":
                                resp = """𝗨𝗦𝗔𝗚𝗘:
𝗧𝗬𝗣𝗘 /masstxt 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 𝗥𝗘𝗣𝗟𝗬 𝗧𝗢 𝗔 𝗧𝗫𝗧 𝗙𝗜𝗟𝗘 𝗪𝗛𝗜𝗖𝗛 𝗖𝗢𝗡𝗧𝗔𝗜𝗡𝗦 𝗖𝗖 𝗜𝗡 𝗢𝗥𝗗𝗘𝗥 𝗧𝗢 𝗨𝗦𝗘 𝗧𝗛𝗜𝗦 𝗚𝗔𝗧𝗘"""
                                await message.reply_text(resp, message.id)
                            elif e == "This message doesn't contain any downloadable media":
                                resp = """𝗨𝗦𝗔𝗚𝗘:
𝗧𝗬𝗣𝗘 /masstxt 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 𝗥𝗘𝗣𝗟𝗬 𝗧𝗢 𝗔 𝗧𝗫𝗧 𝗙𝗜𝗟𝗘 𝗪𝗛𝗜𝗖𝗛 𝗖𝗢𝗡𝗧𝗔𝗜𝗡𝗦 𝗖𝗖 𝗜𝗡 𝗢𝗥𝗗𝗘𝗥 𝗧𝗢 𝗨𝗦𝗘 𝗧𝗛𝗜𝗦 𝗚𝗔𝗧𝗘"""
                                await message.reply_text(resp, message.id)

                        if getfile == "YES":
                            amt = 0
                            file = open(
                                f"downloads/{file_name}").read().splitlines()
                            for i in file:
                                amt += 1
                            all_cards = amt
                            stresp = "𝗦𝗧𝗔𝗥𝗧𝗘𝗗 𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚.."
                            stchk = await message.reply_text(
                                stresp, message.id)
                            if amt > 50 and role == "FREE":
                                resp = "𝗦𝗢𝗥𝗥𝗬 𝗙𝗥𝗘𝗘 𝗨𝗦𝗘𝗥 𝗔𝗥𝗘 𝗟𝗜𝗠𝗜𝗧𝗘𝗗 𝗧𝗢 50 𝗖𝗖 𝗖𝗛𝗘𝗖𝗞 𝗟𝗜𝗠𝗜𝗧 ❌"
                                free = await Client.edit_message_text(
                                    message.chat.id, stchk.id, resp)
                                my_file = Path(f"downloads/{file_name}")
                                my_file.unlink(missing_ok=True)

                            elif amt > 250 and role == 'PREMIUM':
                                resp = "𝗦𝗢𝗥𝗥𝗬 𝗣𝗥𝗘𝗠𝗜𝗨𝗠 𝗠𝗘𝗠𝗕𝗘𝗥𝗦 𝗛𝗔𝗦 250 𝗖𝗖 𝗖𝗛𝗘𝗖𝗞 𝗟𝗜𝗠𝗜𝗧 ❌"
                                PREMIUM = await Client.edit_message_text(
                                    message.chat.id, stchk.id, resp)
                                my_file = Path(f"downloads/{file_name}")
                                my_file.unlink(missing_ok=True)
                            elif amt > 1250 and role == '♥ LIFETIME ♥':
                                resp = "𝗦𝗢𝗥𝗥𝗬 𝗣𝗥𝗘𝗠𝗜𝗨𝗠 𝗠𝗘𝗠𝗕𝗘𝗥𝗦 𝗛𝗔𝗦 1250 𝗖𝗖 𝗖𝗛𝗘𝗖𝗞 𝗟𝗜𝗠𝗜𝗧 ❌"
                                PREMIUM = await Client.edit_message_text(
                                    message.chat.id, stchk.id, resp)
                                my_file = Path(f"downloads/{file_name}")
                                my_file.unlink(missing_ok=True)
                            else:
                                await Client.delete_messages(
                                    message.chat.id, stchk.id)
                                text = f"""
𝗚𝗮𝘁𝗲𝘀: <b>MASS AUTH</b>
𝗧𝗼𝘁𝗮𝗹 𝗖𝗖 𝗜𝗻𝗽𝘂𝘁: <b>{amt}</b>
𝗛𝗶𝘁𝘀: <b>Counting..</b>
𝗗𝗲𝗮𝗱: <b>Counting..</b>
<b>Secret Key:</b> <code>{key}</code>
<i>( if checker got stuck or bot got stopped , then you can easily get your hits.txt file by typing "/gethits secretkey" this commands. )</i>
𝗦𝘁𝗮𝘁𝘂𝘀: <b>Checking</b>

𝗖𝗵𝗲𝗰𝗸𝗲𝗱 𝗕𝘆 <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> 
𝗖𝗿𝗲𝗱𝗶𝘁 𝗪𝗶𝗹𝗹 𝗕𝗲 𝗗𝗲𝗱𝘂𝗰𝘁𝗲𝗱: <b>{amt}</b>
𝗕𝗼𝘁 𝗕𝘆: @stripe_xD"""
                                stats = await message.reply_text(
                                    text, message.id)
                                chk_done = 0
                                hits_count = 0
                                with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
                                    futures = []
                                    for i in file:
                                        future = executor.submit(getmassresult,i,user_id)
                                        futures.append(future)
                                    for future in concurrent.futures.as_completed(futures):
                                        result = future.result()
                                        chk_done += 1
                                        calc = chk_done % 20
                                        if result[1]=="YES":
                                            cc = result[2]
                                            response = result[0]
                                            hits_count += 1
                                            dead = chk_done - hits_count
                                            hitsfile = f"HITS/{file_name}"
                                            with open(hitsfile, "a",encoding="UTF-8") as f:
                                                hitresp = f"{cc}\nResult - {response}\n"
                                                f.write(hitresp)
                                        else:
                                            pass
                                        if calc==0:
                                            cc = result[2]
                                            response = result[0]
                                            dead = chk_done - hits_count
                                            text = f"""
𝗚𝗮𝘁𝗲𝘀: <b>MASS AUTH </b>

<code>{cc}</code>
<b>Result - {response}</b>

𝗧𝗼𝘁𝗮𝗹 𝗖𝗖 𝗜𝗻𝗽𝘂𝘁: <b>{amt}</b>
𝗛𝗶𝘁𝘀: <b>{hits_count} </b>
𝗗𝗲𝗮𝗱: <b>{dead}</b>
<b>Total Checked: {chk_done}</b>
<i>( total checked status will be updated after 10 cc checked done . this is for telegram limitation of message.edit )</i>
<b>Secret Key:</b> <code>{key}</code>
<i>( if checker got stuck or bot got stopped , then you can easily get your hits.txt file by typing "/gethits secretkey" this commands. )</i>
<b>Status: Checking</b>


𝗖𝗵𝗲𝗰𝗸𝗲𝗱 𝗕𝘆 <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> 
𝗖𝗿𝗲𝗱𝗶𝘁 𝗪𝗶𝗹𝗹 𝗕𝗲 𝗗𝗲𝗱𝘂𝗰𝘁𝗲𝗱: <b>{amt} </b>
𝗕𝗼𝘁 𝗕𝘆: @stripe_xD
            """
                                            try:
                                                stats = await Client.edit_message_text(
                                                    message.chat.id, stats.id,
                                                    text)
                                            except Exception as e:
                                                pass
                                        else:
                                            pass
                                dead = chk_done - hits_count 
                                if hits_count != 0:
                                    await Client.delete_messages(
                                        message.chat.id, stats.id)
                                    my_file = Path(f"downloads/{file_name}")
                                    my_file.unlink(missing_ok=True)
                                    text = f"""
𝗚𝗮𝘁𝗲𝘀: <b>MASS AUTH </b>
𝗧𝗼𝘁𝗮𝗹 𝗖𝗖 𝗜𝗻𝗽𝘂𝘁: <b>{amt}</b>
𝗛𝗶𝘁𝘀: <b>{hits_count} </b>
𝗗𝗲𝗮𝗱: <b>{dead}</b>
Total Checked: <b>{chk_done}</b>
<b>Secret Key:</b> <code>{key}</code>
<i>( if checker got stuck or bot got stopped , then you can easily get your hits.txt file by typing "/gethits secretkey" this commands. )</i>
<b>Status: Checked All ✅</b>

𝗖𝗵𝗲𝗰𝗸𝗲𝗱 𝗕𝘆 <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> 
𝗖𝗿𝗲𝗱𝗶𝘁 𝗪𝗶𝗹𝗹 𝗕𝗲 𝗗𝗲𝗱𝘂𝗰𝘁𝗲𝗱: <b>{amt} </b>
𝗕𝗼𝘁 𝗕𝘆: @stripe_xD
"""
                                    all_done = await message.reply_document(
                                        document=hitsfile,
                                        caption=text,
                                        reply_to_message_id=message.id)
                                else:
                                    my_file = Path(f"downloads/{file_name}")
                                    my_file.unlink(missing_ok=True)
                                    text = f"""
𝗚𝗮𝘁𝗲𝘀: <b>MASS AUTH </b>
𝗧𝗼𝘁𝗮𝗹 𝗖𝗖 𝗜𝗻𝗽𝘂𝘁: <b>{amt}</b>
𝗛𝗶𝘁𝘀: <b>{hits_count} </b>
𝗗𝗲𝗮𝗱: <b>{dead}</b>
<b>Total Checked: {chk_done}</b>
<b>Secret Key:</b> <code>{key}</code>
<i>( if checker got stuck or bot got stopped , then you can easily get your hits.txt file by typing "/gethits secretkey" this commands. )</i>
<b>Status: Checked All ✅</b>

𝗖𝗵𝗲𝗰𝗸𝗲𝗱 𝗕𝘆 <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> 
𝗖𝗿𝗲𝗱𝗶𝘁 𝗪𝗶𝗹𝗹 𝗕𝗲 𝗗𝗲𝗱𝘂𝗰𝘁𝗲𝗱: <b>{amt} </b>
𝗕𝗼𝘁 𝗕𝘆: @stripe_xD
"""
                                    stats = await Client.edit_message_text(
                                        message.chat.id, stats.id, text)
                                massdeductcredit(user_id,amt)
                                setantispamtime(user_id)
                                plancheck = plan_expirychk(user_id)
                                if plancheck == "YES":
                                    resp = """
𝗛𝗲𝘆 𝗗𝘂𝗱𝗲 !
𝗬𝗼𝘂𝗿 𝗖𝘂𝗿𝗿𝗲𝗻𝘁 𝗣𝗹𝗮𝗻 𝗛𝗮𝘀 𝗘𝘅𝗽𝗶𝗿𝗲𝗱.𝗧𝗼 𝗥𝗲𝗴𝗮𝗶𝗻 𝗔𝗰𝗰𝗲𝘀𝘀 𝗣𝘂𝗿𝗰𝗵𝗮𝘀𝗲 𝗮𝗴𝗮𝗶𝗻 𝘂𝘀𝗶𝗻𝗴 /buy
                  """
                                    await Client.send_message(user_id, resp)
                                else:
                                    pass
                        else:
                            pass
    # except Exception as e:
    #     with open("error_logs.txt", "a") as f:
    #         f.write(f"{e}\n")
