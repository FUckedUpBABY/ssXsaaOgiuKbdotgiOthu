import asyncio
from pyrogram import Client,filters
import re
from pathlib import Path
from FUNC.defs import *
from FUNC.usersdb_func import *
import asyncio
import threading
plugins = dict(root="bot")

user = Client("scrapper",
              api_id = str(open('FILES/config.txt',encoding="UTF-8").read().splitlines()[0]) ,
              api_hash = str(open('FILES/config.txt',encoding="UTF-8").read().splitlines()[1]) )

bot = Client("my_bot",
             api_id = str(open('FILES/config.txt',encoding="UTF-8").read().splitlines()[0]) ,
             api_hash = str(open('FILES/config.txt',encoding="UTF-8").read().splitlines()[1]) ,
             bot_token = str(open('FILES/config.txt',encoding="UTF-8").read().splitlines()[2]) ,
             plugins = plugins)

@bot.on_message(filters.command("scr", [".","/"]))
async def scr(Client,message):
    try:
        await user.start()
    except Exception as e:
        with open("scr_logs.txt","a",encoding="UTF-8") as f:
            f.write(f"{str(e)}\n")
    try:
        error = ""
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
                resp = "𝐂𝐇𝐀𝐓 𝐈𝐒 𝐍𝐎𝐓 𝐀𝐔𝐓𝐇𝐎𝐑𝐈𝐙𝐄𝐃 𝐓𝐎 𝐔𝐒𝐄 𝐓𝐇𝐈𝐒 𝐂𝐎𝐌𝐌𝐀𝐍𝐃, 𝐀𝐒𝐊 𝐌𝐘 𝐎𝐖𝐍𝐄𝐑 @stripe_xD @@TH_Temp 𝗧𝗢 𝗔𝗨𝗧𝗛𝗢𝗥𝗜𝗭𝗘."
                await message.reply_text(resp, message.id)
            else:
                if credit < 3:
                    resp = "𝐒𝐎𝐑𝐑𝐘 𝐁𝐑𝐎! 𝐑𝐀𝐍 𝐎𝐔𝐓 𝐎𝐅 𝐂𝐑𝐄𝐃𝐈𝐓𝐒 𝐋𝐌𝐀𝐎. 𝐓𝐎 𝐁𝐔𝐘 𝐃𝐦 @stripe_xD"
                    await message.reply_text(resp, message.id)
                else:
                    msg = message.text.split(" ")
                    try:
                        channel_link = msg[1]
                    except Exception as e:
                        error = "YES"
                        resp = f"""
𝐅𝐎𝐑𝐌𝐀𝐓 𝐈𝐍𝐕𝐀𝐋𝐈𝐃

𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒:
𝐭𝐨 𝐒𝐜𝐫𝐚𝐩𝐞 𝐂𝐂 𝐟𝐫𝐨𝐦 𝐏𝐮𝐛𝐥𝐢𝐜 𝐂𝐡𝐚𝐭𝐬
<code>/scr username 69</code>

𝐭𝐨 𝐒𝐜𝐫𝐚𝐩𝐞 𝐂𝐂 𝐟𝐫𝐨𝐦 𝐏𝐫𝐢𝐯𝐚𝐭𝐞 𝐂𝐡𝐚𝐭𝐬
<code>/scr https://t.me/+aG5kczFDfd 69</code>
            """
                        await message.reply_text(resp, message.id)
                    if error != "YES":
                        #
                        try:
                            limit = int(msg[2])
                        except:
                            limit = 100
                        if status == 'FREE' and limit > 30000:

                            resp = f"""
  𝐅𝐫𝐞𝐞 𝐁𝐨𝐳𝐨𝐬 𝐚𝐫𝐞 𝐋𝐢𝐦𝐢𝐭𝐞𝐝 𝐭𝐨 𝟑𝟎𝟎𝟎𝟎 𝐂𝐂 𝐒𝐂𝐑𝐀𝐏𝐄
              """
                            await message.reply_text(resp, message.id)
                        elif status == 'PREMIUM' and limit > 100000:

                            resp = f"""
  𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐔𝐒𝐄𝐑𝐒 𝐂𝐀𝐍 𝐒𝐂𝐑𝐀𝐏𝐄 𝐔𝐏𝐓𝐎 𝟏𝟎𝟎𝐊 𝐂𝐂
              """
                            await message.reply_text(resp, message.id)

                        else:
                            delete = await message.reply_text("𝗦𝗰𝗿𝗮𝗽𝗶𝗻𝗴 𝗪𝗮𝗶𝘁...", message.id)
                            if "https" in channel_link:
                                try:
                                    
                                    join = await user.join_chat(channel_link)
                                    title = join.title
                                    channel_id = join.id
                                    amt_cc = 0
                                    dublicate = 0
                                    async for msg in user.get_chat_history(
                                            channel_id, limit):
                                        all_history = str(msg.text)
                                        if all_history == 'None':
                                            all_history = "INVALID CC NUMBER BC"
                                        else:
                                            all_history = all_history
                                        all_cards = all_history.split('\n')
                                        cards = []
                                        for x in all_cards:
                                            car = getcards(x)
                                            if car:
                                                cards.append(car)
                                            else:
                                                continue
                                        len_cards = len(cards)
                                        if not len_cards:
                                            resp = "𝐑𝐄𝐒𝐔𝐋𝐓 ⟿ 𝐅𝐎𝐔𝐍𝐃 𝐍𝐎 𝐕𝐀𝐋𝐈𝐃 𝐂𝐂"
                                        for item in cards:
                                            amt_cc += 1
                                            cc = item[0]
                                            mes = item[1]
                                            ano = item[2]
                                            cvv = item[3]
                                            fullcc = f"{cc}|{mes}|{ano}|{cvv}"

                                            file_name = f"{limit}x_CC_Scraped_By_@MarsCheckerBot.txt"
                                            with open(file_name, 'a') as f:
                                                cclist = open(
                                                    f"{file_name}").read(
                                                    ).splitlines()
                                                if fullcc in cclist:
                                                    dublicate += 1
                                                else:
                                                    f.write(f"{fullcc}\n")

                                    total_cc = amt_cc
                                    cc_found = total_cc - dublicate
                                    await bot.delete_messages(message.chat.id, delete.id)
                                    caption = f"""
𝐂𝐑𝐄𝐃𝐈𝐓 𝐂𝐀𝐑𝐃 𝐒𝐂𝐑𝐀𝐏𝐏𝐄𝐑 ✅

𝐂𝐇𝐀𝐓 𝐍𝐀𝐌𝐄 {title}
𝐀𝐌𝐎𝐔𝐍𝐓 {limit}
𝐂𝐀𝐑𝐃 𝐒𝐂𝐑𝐀𝐏𝐏𝐄𝐃 {cc_found}
𝐂𝐀𝐑𝐃 𝐑𝐄𝐌𝐎𝐕𝐄𝐃 (𝐃𝐔𝐏𝐋𝐈𝐂𝐀𝐓𝐄𝐒) {dublicate}
𝐑𝐄𝐐𝐔𝐄𝐒𝐓𝐄𝐃 𝐁𝐘 <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> 🗿 [ {status} ]
- 𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 𝐂𝐇𝐄𝐂𝐊𝐄𝐑 𝐁𝐎𝐓 𝐎𝐅 𝐓𝐄𝐀𝐌 𝐍𝐌𝐁
  """
                                    document = file_name
                                    scr_done = await message.reply_document(
                                        document=document,
                                        caption=caption,
                                        reply_to_message_id=message.id)
                                    deductcredit(user_id)

                                    if scr_done:
                                        name = document
                                        my_file = Path(name)
                                        my_file.unlink(missing_ok=True)
                                    
                                except Exception as e:
                                    
                                    e = str(e)
                                    with open("error_logs.txt", "a") as f:

                                        f.write(f"{e}\n")
                                    fr_error = 'Telegram says: [400 USER_ALREADY_PARTICIPANT] - The user is already a participant of this chat (caused by "messages.ImportChatInvite")'
                                    sec_error = 'Telegram says: [400 INVITE_HASH_EXPIRED] - The chat invite link is no longer valid (caused by "messages.ImportChatInvite")'
                                    if e == fr_error:
                                        
                                        chat_info = await user.get_chat(
                                            channel_link)
                                        channel_id = chat_info.id
                                        title = chat_info.title
                                        
                                        try:
                                            
                                            amt_cc = 0
                                            dublicate = 0

                                            async for msg in user.get_chat_history(
                                                    channel_id, limit):
                                                all_history = str(msg.text)
                                                if all_history == 'None':
                                                    all_history = "INVALID CC NUMBER BC"
                                                else:
                                                    all_history = all_history
                                                all_cards = all_history.split(
                                                    '\n')
                                                cards = []
                                                for x in all_cards:
                                                    car = getcards(x)
                                                    if car:
                                                        cards.append(car)
                                                    else:
                                                        continue
                                                len_cards = len(cards)
                                                if not len_cards:
                                                    resp = "𝐑𝐄𝐒𝐔𝐋𝐓 ⟿ 𝐅𝐎𝐔𝐍𝐃 𝐍𝐎 𝐕𝐀𝐋𝐈𝐃 𝐂𝐂"
                                                for item in cards:
                                                    amt_cc += 1
                                                    cc = item[0]
                                                    mes = item[1]
                                                    ano = item[2]
                                                    cvv = item[3]
                                                    fullcc = f"{cc}|{mes}|{ano}|{cvv}"

                                                    file_name = f"{limit}x_CC_Scraped_By_@MarsCheckerBot.txt"
                                                    with open(file_name,
                                                              'a') as f:
                                                        cclist = open(
                                                            f"{file_name}"
                                                        ).read().splitlines()
                                                        if fullcc in cclist:
                                                            dublicate += 1
                                                        else:
                                                            f.write(
                                                                f"{fullcc}\n")

                                            total_cc = amt_cc
                                            cc_found = total_cc - dublicate
                                            await bot.delete_messages(
                                                message.chat.id, delete.id)
                                            caption = f"""
𝐂𝐑𝐄𝐃𝐈𝐓 𝐂𝐀𝐑𝐃 𝐒𝐂𝐑𝐀𝐏𝐏𝐄𝐑 ✅

𝐂𝐇𝐀𝐓 𝐍𝐀𝐌𝐄 {title}
𝐀𝐌𝐎𝐔𝐍𝐓 {limit}
𝐂𝐀𝐑𝐃 𝐒𝐂𝐑𝐀𝐏𝐏𝐄𝐃 {cc_found}
𝐂𝐀𝐑𝐃 𝐑𝐄𝐌𝐎𝐕𝐄𝐃 (𝐃𝐔𝐏𝐋𝐈𝐂𝐀𝐓𝐄𝐒) {dublicate}
𝐑𝐄𝐐𝐔𝐄𝐒𝐓𝐄𝐃 𝐁𝐘 <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> 🗿 [ {status} ]
- 𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 𝐂𝐇𝐄𝐂𝐊𝐄𝐑 𝐁𝐎𝐓 𝐎𝐅 𝐓𝐄𝐀𝐌 𝐍𝐌𝐁
  """
                                            document = file_name
                                            scr_done = await message.reply_document(
                                                document=document,
                                                caption=caption,
                                                reply_to_message_id=message.id)
                                            deductcredit(user_id)

                                            if scr_done:
                                                name = document
                                                my_file = Path(name)
                                                my_file.unlink(missing_ok=True)
                                            
                                        except Exception as e:
                                            
                                            with open("error_logs.txt",
                                                      "a") as f:
                                                f.write(f"{e}\n")

                                            await bot.delete_messages(
                                                message.chat.id, delete.id)
                                            await message.reply_text(
                                                e, message.id)
                                    elif e == sec_error:
                                        resp = "𝗪𝗿𝗼𝗻𝗴 𝗜𝗻𝘃𝗶𝘁𝗲 𝗟𝗶𝗻𝗸 ❌"
                                        await bot.delete_messages(
                                            message.chat.id, delete.id)
                                        await message.reply_text(
                                            resp, message.id)
                                    else:
                                        await bot.delete_messages(
                                            message.chat.id, delete.id)
                                        await message.reply_text(e, message.id)
                            else:
                                try:
                                    
                                    amt_cc = 0
                                    dublicate = 0

                                    async for msg in user.get_chat_history(
                                            channel_link, limit):
                                        all_history = str(msg.text)
                                        if all_history == 'None':
                                            all_history = "INVALID CC NUMBER BC"
                                        else:
                                            all_history = all_history
                                        all_cards = all_history.split('\n')
                                        cards = []
                                        for x in all_cards:
                                            car = getcards(x)
                                            if car:
                                                cards.append(car)
                                            else:
                                                continue
                                        len_cards = len(cards)
                                        if not len_cards:
                                            resp = "𝐑𝐄𝐒𝐔𝐋𝐓 ⟿ 𝐅𝐎𝐔𝐍𝐃 𝐍𝐎 𝐕𝐀𝐋𝐈𝐃 𝐂𝐂"
                                        for item in cards:
                                            amt_cc += 1
                                            cc = item[0]
                                            mes = item[1]
                                            ano = item[2]
                                            cvv = item[3]
                                            fullcc = f"{cc}|{mes}|{ano}|{cvv}"

                                            file_name = f"{limit}x_CC_Scraped_By_@MarsCheckerBot.txt"
                                            with open(file_name, 'a') as f:
                                                cclist = open(
                                                    f"{file_name}").read(
                                                    ).splitlines()
                                                if fullcc in cclist:
                                                    dublicate += 1
                                                else:
                                                    f.write(f"{fullcc}\n")

                                    chat_info = await user.get_chat(
                                        channel_link)
                                    title = chat_info.title
                                    total_cc = amt_cc
                                    cc_found = total_cc - dublicate
                                    await bot.delete_messages(chat_id=message.chat.id, message_ids=delete.id)
                                    caption = f"""
𝐂𝐑𝐄𝐃𝐈𝐓 𝐂𝐀𝐑𝐃 𝐒𝐂𝐑𝐀𝐏𝐏𝐄𝐑 ✅

𝐂𝐇𝐀𝐓 𝐍𝐀𝐌𝐄 {title}
𝐀𝐌𝐎𝐔𝐍𝐓 {limit}
𝐂𝐀𝐑𝐃 𝐒𝐂𝐑𝐀𝐏𝐏𝐄𝐃 {cc_found}
𝐂𝐀𝐑𝐃 𝐑𝐄𝐌𝐎𝐕𝐄𝐃 (𝐃𝐔𝐏𝐋𝐈𝐂𝐀𝐓𝐄𝐒) {dublicate}
𝐑𝐄𝐐𝐔𝐄𝐒𝐓𝐄𝐃 𝐁𝐘 <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> 🗿 [ {status} ]
- 𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 𝐂𝐇𝐄𝐂𝐊𝐄𝐑 𝐁𝐎𝐓 𝐎𝐅 𝐓𝐄𝐀𝐌 𝐍𝐌𝐁
  """
                                    document = file_name
                                    scr_done = await message.reply_document(
                                        document=document,
                                        caption=caption,
                                        reply_to_message_id=message.id)
                                    deductcredit(user_id)

                                    if scr_done:
                                        name = document
                                        my_file = Path(name)
                                        my_file.unlink(missing_ok=True)
                                    
                                except Exception as e:
                                    
                                    with open("error_logs.txt", "a") as f:
                                        f.write(f"{e}\n")
                                    e = str(e)
                                    first_error = "Error : local variable 'file_name' referenced before assignment"
                                    sec_error = 'Telegram says: [400 USERNAME_NOT_OCCUPIED] - The username is not occupied by anyone (caused by "contacts.ResolveUsername")'
                                    third_error = "local variable 'file_name' referenced before assignment"
                                    fourth_error = 'Telegram says: [400 USERNAME_INVALID] - The username is invalid (caused by "contacts.ResolveUsername")'
                                    if e == first_error:
                                        resp = "No CC Found"
                                        await bot.delete_messages(
                                            message.chat.id, delete.id)
                                        await message.reply_text(
                                            text=resp,
                                            reply_to_message_id=message.id)
                                    elif e == sec_error:
                                        resp = "𝗪𝗿𝗼𝗻𝗴 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 ❌"
                                        await bot.delete_messages(
                                            message.chat.id, delete.id)
                                        await message.reply_text(
                                            text=resp,
                                            reply_to_message_id=message.id)
                                    elif e == third_error:
                                        resp = "𝗡𝗼 𝗖𝗖 𝗙𝗼𝘂𝗻𝗱 ❌"
                                        await bot.delete_messages(
                                            message.chat.id, delete.id)
                                        await message.reply_text(
                                            text=resp,
                                            reply_to_message_id=message.id)
                                    elif e == fourth_error:
                                        resp = "𝗪𝗿𝗼𝗻𝗴 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 ❌"
                                        await bot.delete_messages(
                                            message.chat.id, delete.id)
                                        await message.reply_text(
                                            text=resp,
                                            reply_to_message_id=message.id)
                                    else:
                                        await bot.delete_messages(
                                            message.chat.id, delete.id)
                                        await message.reply_text(
                                            text=e,
                                            reply_to_message_id=message.id)
    # try:
    #     await user.stop()
    # except:
    #     pass
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")
    try:
        await user.stop()
    except Exception as e:
        with open("scr_logs.txt","a",encoding="UTF-8") as f:
            f.write(f"{str(e)}\n")


@bot.on_message(filters.command("scrsk", [".","/"]))
async def skscr(Client,message):
    try:
        await user.start()
    except Exception as e:
        with open("scr_logs.txt","a",encoding="UTF-8") as f:
            f.write(f"{str(e)}\n")
    try:
        error = ""
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
                resp = "𝐔𝐍𝐀𝐔𝐓𝐇𝐎𝐑𝐈𝐙𝐄𝐃 𝐔𝐒𝐄𝐑 𝐋𝐌𝐀𝐎! 𝐑𝐔𝐍 𝐁𝐎𝐙𝐎 𝐑𝐔𝐍"
                await message.reply_text(resp, message.id)

            elif chat_type == "ChatType.GROUP" or chat_type == "ChatType.SUPERGROUP" and checkgroup == "None":
                resp = "𝐂𝐇𝐀𝐓 𝐈𝐒 𝐍𝐎𝐓 𝐀𝐔𝐓𝐇𝐎𝐑𝐈𝐙𝐄𝐃, 𝐓𝐎 𝐔𝐒𝐄 𝐓𝐇𝐈𝐒 𝐂𝐎𝐌𝐌𝐀𝐍𝐃, 𝐀𝐒𝐊 𝐌𝐘 𝐎𝐖𝐍𝐄𝐑 @stripe_xD 𝗧𝗢 𝗔𝗨𝗧𝗛𝗢𝗥𝗜𝗭𝗘."
                await message.reply_text(resp, message.id)
            else:
                if credit < 3:
                    resp = "𝐒𝐎𝐑𝐑𝐘 𝐁𝐑𝐎! 𝐑𝐀𝐍 𝐎𝐔𝐓 𝐎𝐅 𝐂𝐑𝐄𝐃𝐈𝐓𝐒 𝐋𝐌𝐀𝐎. 𝐓𝐎 𝐁𝐔𝐘 𝐃𝐦 @stripe_xD"
                    await message.reply_text(resp, message.id)
                else:
                    msg = message.text.split(" ")
                    try:
                        channel_link = msg[1]
                    except Exception as e:
                        error = "YES"
                        resp = f"""
𝐅𝐎𝐑𝐌𝐀𝐓 𝐈𝐍𝐕𝐀𝐋𝐈𝐃

𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒:
𝐭𝐨 𝐒𝐜𝐫𝐚𝐩𝐞 𝐂𝐂 𝐟𝐫𝐨𝐦 𝐏𝐮𝐛𝐥𝐢𝐜 𝐂𝐡𝐚𝐭𝐬
<code>/scrsk username 69</code>

𝐭𝐨 𝐒𝐜𝐫𝐚𝐩𝐞 𝐂𝐂 𝐟𝐫𝐨𝐦 𝐏𝐫𝐢𝐯𝐚𝐭𝐞 𝐂𝐡𝐚𝐭𝐬
<code>/scrsk https://t.me/+aWGWWWRGS43z 69</code>
            """
                        await message.reply_text(resp, message.id)
                    if error != "YES":
                        #
                        try:
                            limit = int(msg[2])
                        except:
                            limit = 100
                        if status == 'FREE' and limit > 30000:

                            resp = f"""
  𝐅𝐫𝐞𝐞 𝐁𝐨𝐳𝐨𝐬 𝐚𝐫𝐞 𝐋𝐢𝐦𝐢𝐭𝐞𝐝 𝐭𝐨 𝟯𝟬𝟬𝟬𝟬 𝐂𝐂 𝐒𝐂𝐑𝐀𝐏𝐄
              """
                            await message.reply_text(resp, message.id)
                        elif status == 'PREMIUM' and limit > 100000:

                            resp = f"""
  𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐔𝐒𝐄𝐑𝐒 𝐂𝐀𝐍 𝐒𝐂𝐑𝐀𝐏𝐄 𝐔𝐏𝐓𝐎 𝟏𝟎𝟎𝐊 𝐂𝐂
              """
                            await message.reply_text(resp, message.id)

                        else:
                            delete = await message.reply_text("𝗦𝗰𝗿𝗮𝗽𝗶𝗻𝗴 𝗪𝗮𝗶𝘁...", message.id)
                            if "https" in channel_link:
                                try:
                                    
                                    join = await user.join_chat(channel_link)
                                    title = join.title
                                    channel_id = join.id
                                    amt_cc = 0
                                    dublicate = 0
                                    sks = []
                                    async for msg in user.get_chat_history(channel_id, limit):
                                        all_history = str(msg.text)
                                        if all_history == 'None':
                                            all_history = "INVALID CC NUMBER BC"
                                        else:
                                            all_history = all_history
                                        if "sk_live" in all_history:
                                            amt_cc += 1
                                            sk = all_history.split("sk_live")[1].split(" ")[0]
                                            if "\n" in sk:
                                                sk = sk.split("\n")[0]
                                            if "✅" in sk:
                                                sk = sk.splice("✅")[1]
                                            sk = "sk_live_" + sk 
                                            sks.append(sk)
                                        else:
                                            pass

                                    if len(sks)==0:
                                        resp = "NO SK FOUND"
                                        await message.reply_text(resp, message.id)
                                    else:
                                        file_name = f"{limit}x_SK_Scraped_By_@MarsCheckerBot.txt"
                                        for x in sks:
                                            with open(file_name, 'a') as f:
                                                cclist = open(f"{file_name}").read().splitlines()
                                                if x in cclist:
                                                    dublicate += 1
                                                else:
                                                    f.write(f"{x}\n")

                                    total_cc = amt_cc
                                    cc_found = total_cc - dublicate
                                    await bot.delete_messages(message.chat.id, delete.id)
                                    caption = f"""
𝐒𝐓𝐑𝐈𝐏𝐄 𝐊𝐄𝐘 (𝐒𝐊) 𝐒𝐂𝐑𝐀𝐏𝐏𝐄𝐑 ✅

𝐂𝐇𝐀𝐓 𝐍𝐀𝐌𝐄 {title}
𝐀𝐌𝐎𝐔𝐍𝐓 {limit}
𝐒𝐓𝐑𝐈𝐏𝐄 𝐊𝐄𝐘 (𝐒𝐊) 𝐅𝐎𝐔𝐍𝐃 {cc_found}
𝐑𝐄𝐐𝐔𝐄𝐒𝐓𝐄𝐃 𝐁𝐘 <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> 🗿 [ {status} ]
- 𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 𝐂𝐇𝐄𝐂𝐊𝐄𝐑 𝐁𝐎𝐓 𝐎𝐅 𝐓𝐄𝐀𝐌 𝐍𝐌𝐁
  """
                                    document = file_name
                                    scr_done = await message.reply_document(
                                        document=document,
                                        caption=caption,
                                        reply_to_message_id=message.id)
                                    deductcredit(user_id)

                                    if scr_done:
                                        name = document
                                        my_file = Path(name)
                                        my_file.unlink(missing_ok=True)
                                    
                                except Exception as e:
                                    
                                    e = str(e)
                                    with open("error_logs.txt", "a") as f:

                                        f.write(f"{e}\n")
                                    fr_error = 'Telegram says: [400 USER_ALREADY_PARTICIPANT] - The user is already a participant of this chat (caused by "messages.ImportChatInvite")'
                                    sec_error = 'Telegram says: [400 INVITE_HASH_EXPIRED] - The chat invite link is no longer valid (caused by "messages.ImportChatInvite")'
                                    if e == fr_error:
                                        
                                        chat_info = await user.get_chat(
                                            channel_link)
                                        channel_id = chat_info.id
                                        title = chat_info.title
                                        
                                        try:
                                            
                                            amt_cc = 0
                                            dublicate = 0
                                            sks = []
                                            async for msg in user.get_chat_history(
                                                    channel_id, limit):
                                                all_history = str(msg.text)
                                                if all_history == 'None':
                                                    all_history = "INVALID CC NUMBER BC"
                                                else:
                                                    all_history = all_history
                                                if "sk_live" in all_history:
                                                    amt_cc += 1
                                                    sk = all_history.split("sk_live")[1].split(" ")[0]
                                                    if "\n" in sk:
                                                        sk = sk.split("\n")[0]
                                                    if "✅" in sk:
                                                        sk = sk.splice("✅")[1]
                                                    sk = "sk_live_" + sk 
                                                    sks.append(sk)
                                                else:
                                                    pass

                                            if len(sks)==0:
                                                resp = "NO SK FOUND"
                                                await message.reply_text(resp, message.id)
                                            else:
                                                file_name = f"{limit}x_SK_Scraped_By_@MarsCheckerBot.txt"
                                                for x in sks:
                                                    with open(file_name, 'a') as f:
                                                        cclist = open(f"{file_name}").read().splitlines()
                                                        if x in cclist:
                                                            dublicate += 1
                                                        else:
                                                            f.write(f"{x}\n")

                                            total_cc = amt_cc
                                            cc_found = total_cc - dublicate
                                            await bot.delete_messages(
                                                message.chat.id, delete.id)
                                            caption = f"""
𝐒𝐓𝐑𝐈𝐏𝐄 𝐊𝐄𝐘 (𝐒𝐊) 𝐒𝐂𝐑𝐀𝐏𝐏𝐄𝐑 ✅

𝐂𝐇𝐀𝐓 𝐍𝐀𝐌𝐄 {title}
𝐀𝐌𝐎𝐔𝐍𝐓 {limit}
𝐒𝐓𝐑𝐈𝐏𝐄 𝐊𝐄𝐘 (𝐒𝐊) 𝐅𝐎𝐔𝐍𝐃 {cc_found}
𝐑𝐄𝐐𝐔𝐄𝐒𝐓𝐄𝐃 𝐁𝐘 <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> 🗿 [ {status} ]
- 𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 𝐂𝐇𝐄𝐂𝐊𝐄𝐑 𝐁𝐎𝐓 𝐎𝐅 𝐓𝐄𝐀𝐌 𝐍𝐌𝐁
  """
                                            document = file_name
                                            scr_done = await message.reply_document(
                                                document=document,
                                                caption=caption,
                                                reply_to_message_id=message.id)
                                            deductcredit(user_id)

                                            if scr_done:
                                                name = document
                                                my_file = Path(name)
                                                my_file.unlink(missing_ok=True)
                                            
                                        except Exception as e:
                                            
                                            with open("error_logs.txt",
                                                      "a") as f:
                                                f.write(f"{e}\n")

                                            await bot.delete_messages(
                                                message.chat.id, delete.id)
                                            await message.reply_text(
                                                e, message.id)
                                    elif e == sec_error:
                                        resp = "𝗪𝗿𝗼𝗻𝗴 𝗜𝗻𝘃𝗶𝘁𝗲 𝗟𝗶𝗻𝗸 ❌"
                                        await bot.delete_messages(
                                            message.chat.id, delete.id)
                                        await message.reply_text(
                                            resp, message.id)
                                    else:
                                        await bot.delete_messages(
                                            message.chat.id, delete.id)
                                        await message.reply_text(e, message.id)
                            else:
                                try:
                                    
                                    amt_cc = 0
                                    dublicate = 0
                                    sks = []
                                    async for msg in user.get_chat_history(channel_link, limit):
                                        all_history = str(msg.text)
                                        if all_history == 'None':
                                            all_history = "INVALID CC NUMBER BC"
                                        else:
                                            all_history = all_history
                                        if "sk_live" in all_history:
                                            amt_cc += 1
                                            sk = all_history.split("sk_live")[1].split(" ")[0]
                                            if "\n" in sk:
                                                sk = sk.split("\n")[0]
                                            if "✅" in sk:
                                                sk = sk.splice("✅")[1]
                                            sk = "sk_live_" + sk 
                                            sks.append(sk)
                                        else:
                                            pass

                                    if len(sks)==0:
                                        resp = "NO SK FOUND"
                                        await message.reply_text(resp, message.id)
                                    else:
                                        file_name = f"{limit}x_SK_Scraped_By_@MarsCheckerBot.txt"
                                        for x in sks:
                                            with open(file_name, 'a') as f:
                                                cclist = open(f"{file_name}").read().splitlines()
                                                if x in cclist:
                                                    dublicate += 1
                                                else:
                                                    f.write(f"{x}\n")

                                        chat_info = await user.get_chat(channel_link)
                                        title = chat_info.title
                                        total_cc = amt_cc
                                        cc_found = total_cc - dublicate
                                        await bot.delete_messages(chat_id=message.chat.id, message_ids=delete.id)
                                        caption = f"""
𝐒𝐓𝐑𝐈𝐏𝐄 𝐊𝐄𝐘 (𝐒𝐊) 𝐒𝐂𝐑𝐀𝐏𝐏𝐄𝐑 ✅

𝐂𝐇𝐀𝐓 𝐍𝐀𝐌𝐄 {title}
𝐀𝐌𝐎𝐔𝐍𝐓 {limit}
𝐒𝐓𝐑𝐈𝐏𝐄 𝐊𝐄𝐘 (𝐒𝐊) 𝐅𝐎𝐔𝐍𝐃 {cc_found}
𝐑𝐄𝐐𝐔𝐄𝐒𝐓𝐄𝐃 𝐁𝐘 <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> 🗿 [ {status} ]
- 𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 𝐂𝐇𝐄𝐂𝐊𝐄𝐑 𝐁𝐎𝐓 𝐎𝐅 𝐓𝐄𝐀𝐌 𝐍𝐌𝐁
    """
                                        document = file_name
                                        scr_done = await message.reply_document(
                                            document=document,
                                            caption=caption,
                                            reply_to_message_id=message.id)
                                        deductcredit(user_id)

                                        if scr_done:
                                            name = document
                                            my_file = Path(name)
                                            my_file.unlink(missing_ok=True)
                                        
                                except Exception as e:
                                    
                                    with open("error_logs.txt", "a") as f:
                                        f.write(f"{e}\n")
                                    e = str(e)
                                    first_error = "Error : local variable 'file_name' referenced before assignment"
                                    sec_error = 'Telegram says: [400 USERNAME_NOT_OCCUPIED] - The username is not occupied by anyone (caused by "contacts.ResolveUsername")'
                                    third_error = "local variable 'file_name' referenced before assignment"
                                    fourth_error = 'Telegram says: [400 USERNAME_INVALID] - The username is invalid (caused by "contacts.ResolveUsername")'
                                    if e == first_error:
                                        resp = "No CC Found"
                                        await bot.delete_messages(
                                            message.chat.id, delete.id)
                                        await message.reply_text(
                                            text=resp,
                                            reply_to_message_id=message.id)
                                    elif e == sec_error:
                                        resp = "𝗪𝗿𝗼𝗻𝗴 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 ❌"
                                        await bot.delete_messages(
                                            message.chat.id, delete.id)
                                        await message.reply_text(
                                            text=resp,
                                            reply_to_message_id=message.id)
                                    elif e == third_error:
                                        resp = "𝗡𝗼 𝗦𝗞 𝗙𝗼𝘂𝗻𝗱 ❌"
                                        await bot.delete_messages(
                                            message.chat.id, delete.id)
                                        await message.reply_text(
                                            text=resp,
                                            reply_to_message_id=message.id)
                                    elif e == fourth_error:
                                        resp = "𝗪𝗿𝗼𝗻𝗴 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 ❌"
                                        await bot.delete_messages(
                                            message.chat.id, delete.id)
                                        await message.reply_text(
                                            text=resp,
                                            reply_to_message_id=message.id)
                                    else:
                                        await bot.delete_messages(
                                            message.chat.id, delete.id)
                                        await message.reply_text(
                                            text=e,
                                            reply_to_message_id=message.id)

    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")
    try:
        await user.stop()
    except Exception as e:
        with open("scr_logs.txt","a",encoding="UTF-8") as f:
            f.write(f"{str(e)}\n")