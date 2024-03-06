from pyrogram import Client, filters
import requests
import json
import re
import time
from FUNC.usersdb_func import *
import requests
import json

session = requests.session()


@Client.on_message(filters.command("bin", [".", "/"]))
async def cmd_bin(Client, message):
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
                msg = message.text.split(" ")
                try:
                    try:
                        bin = msg[1]
                    except:
                        bin = message.reply_to_message.text
                except Exception as e:
                    resp = "𝗚𝗜𝗩𝗘 𝗔 𝗩𝗔𝗟𝗜𝗗 𝗕𝗜𝗡 ❌"
                    await message.reply_text(resp, message.id)
                fbin = bin[:6]
                session = requests.session()
                bin = session.get(f"https://lookup.binlist.net/{fbin}").json()
                try:
                    brand = bin["scheme"].upper()
                except:
                    brand = "N/A"
                try:
                    type = bin["type"].upper()
                except:
                    type = "N/A"
                try:
                    level = bin["brand"].upper()
                except:
                    level = "N/A"
                try:
                    bank_data = bin["bank"]
                except:
                    bank_data = "N/A"
                try:
                    bank = bank_data["name"].upper()
                except:
                    bank = "N/A"
                try:
                    country_data = bin["country"]
                except:
                    country_data = "N/A"
                try:
                    country = country_data["name"].upper()
                except:
                    country = "N/A"
                try:
                    flag = country_data["emoji"]
                except:
                    flag = "N/A"
                try:
                    currency = country_data["currency"].upper()
                except:
                    currency = "N/A"
                resp = f"""
𝐂𝐀𝐑𝐃/𝐁𝐈𝐍𝐒 𝐈𝐍𝐅𝐎 ✅

𝗕𝗜𝗡:  <code>{fbin}</code>
𝗕𝗿𝗮𝗻𝗱: {brand}
𝗟𝗲𝘃𝗲𝗹: {level}
𝗧𝘆𝗽𝗲: {type}
𝗕𝗮𝗻𝗸: {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {country} - {flag} - {currency}

𝐑𝐄𝐐𝐔𝐄𝐒𝐓𝐄𝐃 𝐁𝐘-<a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ]
𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 𝐂𝐇𝐄𝐂𝐊𝐄𝐑 𝐁𝐎𝐓 𝐎𝐅 𝐓𝐄𝐀𝐌 𝐍𝐌𝐁
        """
                await message.reply_text(resp, message.id)
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
