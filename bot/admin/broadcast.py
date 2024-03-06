from pyrogram import Client, filters
from FUNC.usersdb_func import *
import threading
import asyncio
import time
from datetime import timedelta


@Client.on_message(filters.command("brod", [".", "/"]))
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
        CEO = "5371579102"
        owner = "5371579102"
        sent_brod = 0
        not_sent = 0
        if user_id != CEO:
            resp = "𝙈𝙛 𝙔𝙤𝙪 𝙖𝙧𝙚 𝙉𝙤𝙩 𝙩𝙝𝙚 𝙊𝙬𝙣𝙚𝙧"
            msg1 = await message.reply_text(resp, message.id)
        else:
            text = "<b>BROADCAST STARTED SUCCESSFULLY ✅</b>"
            await message.reply_text(text, message.id)
            getresp = open("FILES/brod.txt",encoding="UTF-8").read()
            resp = f"<b>{getresp}</b>"
            get_all_user = getallusers()
            total_user = 0
            not_sent = 0
            tic = time.perf_counter()
            for item in get_all_user:
                try:
                    chat_id = int(item["id"])
                    total_user += 1
                    await Client.send_message(chat_id,
                                              resp,
                                              disable_web_page_preview=True)
                except Exception as e:
                    not_sent += 1

            sent_brod = total_user - not_sent
            toc = time.perf_counter()
            sec = toc - tic
            td = str(timedelta(seconds=sec)).split(':')
            hour = td[0]
            min = td[1]
            done = f"""<b>
Brodcast Done ✅
Total User: {total_user}
Message Sent : {sent_brod}
Unable To Sent : {not_sent}
TIME TAKEN : {hour} HOUR {min} MINUTES
     </b> """

            await message.reply_text(done, message.id)
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")
