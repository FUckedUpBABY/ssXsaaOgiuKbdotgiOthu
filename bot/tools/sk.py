from pyrogram import Client, filters
import requests
from FUNC.usersdb_func import *
from FUNC.skfunc import *


@Client.on_message(filters.command("sk", [".", "/"]))
async def cmd_add(Client, message):
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
                resp = "𝐂𝐇𝐀𝐓 𝐈𝐒 𝐍𝐎𝐓 𝐀𝐔𝐓𝐇𝐎𝐑𝐈𝐙𝐄𝐃 𝐓𝐎 𝐔𝐒𝐄 𝐓𝐇𝐈𝐒 𝐂𝐎𝐌𝐌𝐀𝐍𝐃, 𝐀𝐒𝐊 𝐌𝐘 𝐎𝐖𝐍𝐄𝐑 @stripe_xD "
                await message.reply_text(resp, message.id)
            else:
                msg = message.text.split(" ")
                try:
                    try:
                        sk = msg[1]
                    except:
                        sk = message.reply_to_message.text
                except Exception as e:
                    error = "YES"
                    resp = "𝗣𝗟𝗘𝗔𝗦𝗘 𝗣𝗥𝗢𝗩𝗜𝗗𝗘 𝗔 𝗦𝗞 𝗞𝗘𝗬 𝗧𝗢 𝗖𝗛𝗘𝗖𝗞 ⚠️"
                    await message.reply_text(resp, message.id)
                if error != "YES":
                    chkst = "𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝗬𝗼𝘂𝗿 𝗦𝗞 𝗪𝗮𝗶𝘁...."
                    done = await message.reply_text(chkst, message.id)
                    try:
                        import stripe
                        stripe.api_key = sk
                        cc = "5326102318247350|03|2026|627"
                        splitter = cc.split('|')
                        cc_num = splitter[0]
                        mes = splitter[1]
                        ano = splitter[2]
                        cvv = splitter[3]
                        pm = stripe.PaymentMethod.create(
                            type="card",
                            card={
                                "number": f"{cc_num}",
                                "exp_month": f"{mes}",
                                "exp_year": f"{ano}",
                                "cvc": f"{cvv}",
                            },
                        )
                        result = "LIVE"
                    except Exception as e:
                        result = str(e)

                    if result == "LIVE":
                        getskbalance = getbalance(sk)
                        currency = getskbalance[0]
                        balance = getskbalance[1]
                        cards = getskbalance[2]
                        getinfo = getskinfo(sk)
                        usersipresp = getinfo[0]
                        cardbinresp = getinfo[1]
                        cardcountryresp = getinfo[2]
                        ipcountryresp = getinfo[3]
                        resp = f"""<b>
𝗟𝗜𝗩𝗘 𝗞𝗘𝗬 ✅

𝐒𝐓𝐑𝐈𝐏𝐄 𝐊𝐄𝐘 ⟿ <code>{sk}</code>
𝐒𝐓𝐀𝐓𝐔𝐒 ⟿ SK LIVE 💚

𝐒𝐊 𝐈𝐍𝐅𝐎 ⟿
𝐂𝐔𝐑𝐑𝐄𝐍𝐂𝐘 ⟿ {currency}
𝐒𝐊 𝐁𝐀𝐋𝐀𝐍𝐂𝐄 ⟿ {balance}$
𝐏𝐄𝐍𝐃𝐈𝐍𝐆 𝐂𝐂 ⟿ {cards}

𝐆𝐄𝐍𝐄𝐑𝐀𝐋 𝐈𝐍𝐅𝐎 ⟿
{usersipresp}
{cardbinresp}
{cardcountryresp}
{ipcountryresp}

𝐑𝐄𝐐𝐔𝐄𝐒𝐓𝐄𝐃 𝐁𝐘-<a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ]
𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 𝐂𝐇𝐄𝐂𝐊𝐄𝐑 𝐁𝐎𝐓 𝐎𝐅 𝐓𝐄𝐀𝐌 𝐍𝐌𝐁
            </b>"""
                    elif "rate limit" in result:
                        getskbalance = getbalance(sk)
                        currency = getskbalance[0]
                        balance = getskbalance[1]
                        cards = getskbalance[2]
                        getinfo = getskinfo(sk)
                        usersipresp = getinfo[0]
                        cardbinresp = getinfo[1]
                        cardcountryresp = getinfo[2]
                        ipcountryresp = getinfo[3]
                        resp = f"""<b>
𝗟𝗜𝗩𝗘 𝗞𝗘𝗬 ✅

𝐒𝐓𝐑𝐈𝐏𝐄 𝐊𝐄𝐘 ⟿ <code>{sk}</code>
𝐒𝐓𝐀𝐓𝐔𝐒 ⟿ ♻️ 𝗥𝗔𝗧𝗘 𝗟𝗜𝗠𝗜𝗧𝗘𝗗

𝐒𝐊 𝐈𝐍𝐅𝐎 ⟿
𝐂𝐔𝐑𝐑𝐄𝐍𝐂𝐘 ⟿ {currency}
𝐒𝐊 𝐁𝐀𝐋𝐀𝐍𝐂𝐄 ⟿ {balance}$
𝐏𝐄𝐍𝐃𝐈𝐍𝐆 𝐂𝐂 ⟿ {cards}

𝐆𝐄𝐍𝐄𝐑𝐀𝐋 𝐈𝐍𝐅𝐎 ⟿
{usersipresp}
{cardbinresp}
{cardcountryresp}
{ipcountryresp}

𝐑𝐄𝐐𝐔𝐄𝐒𝐓𝐄𝐃 𝐁𝐘-<a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ]
𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 𝐂𝐇𝐄𝐂𝐊𝐄𝐑 𝐁𝐎𝐓 𝐎𝐅 𝐓𝐄𝐀𝐌 𝐍𝐌𝐁
            </b>"""

                    elif "Invalid API Key" in result:
                        resp = f"""<b>
𝗗𝗘𝗔𝗗 𝗞𝗘𝗬 ❌

𝐒𝐓𝐑𝐈𝐏𝐄 𝐊𝐄𝐘 ⟿ <code>{sk}</code>
𝐒𝐓𝐀𝐓𝐔𝐒 ⟿ 𝐌𝐅 𝐆𝐈𝐕𝐄𝐍 𝐈𝐍𝐕𝐀𝐋𝐈𝐃 𝐊𝐄𝐘! ❌

𝐑𝐄𝐐𝐔𝐄𝐒𝐓𝐄𝐃 𝐁𝐘-<a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ]
𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 𝐂𝐇𝐄𝐂𝐊𝐄𝐑 𝐁𝐎𝐓 𝐎𝐅 𝐓𝐄𝐀𝐌 𝐍𝐌𝐁
            </b>"""
                    elif "Expired API Key provided" in result:
                        resp = f"""<b>
𝗗𝗘𝗔𝗗 𝗞𝗘𝗬 ❌

𝐒𝐓𝐑𝐈𝐏𝐄 𝐊𝐄𝐘 ⟿ <code>{sk}</code>
𝐒𝐓𝐀𝐓𝐔𝐒 ⟿ 𝐁𝐀𝐃 𝐋𝐔𝐂𝐊, 𝐒𝐊 𝐄𝐗𝐏𝐈𝐑𝐄𝐃! ❌

𝐑𝐄𝐐𝐔𝐄𝐒𝐓𝐄𝐃 𝐁𝐘-<a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ]
𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 𝐂𝐇𝐄𝐂𝐊𝐄𝐑 𝐁𝐎𝐓 𝐎𝐅 𝐓𝐄𝐀𝐌 𝐍𝐌𝐁
            </b>"""
                    elif "Your account cannot currently make live charges." in result:
                        resp = f"""<b>
𝗗𝗘𝗔𝗗 𝗞𝗘𝗬 ❌

𝐒𝐓𝐑𝐈𝐏𝐄 𝐊𝐄𝐘 ⟿ <code>{sk}</code>
𝐒𝐓𝐀𝐓𝐔𝐒 ⟿ 𝐁𝐀𝐃 𝐋𝐔𝐂𝐊, 𝐓𝐄𝐒𝐓𝐌𝐎𝐃𝐄 𝐒𝐊! ❌

𝐑𝐄𝐐𝐔𝐄𝐒𝐓𝐄𝐃 𝐁𝐘-<a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ]
𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 𝐂𝐇𝐄𝐂𝐊𝐄𝐑 𝐁𝐎𝐓 𝐎𝐅 𝐓𝐄𝐀𝐌 𝐍𝐌𝐁
          </b> """
                    else:
                        resp = f"""<b>
𝗗𝗘𝗔𝗗 𝗞𝗘𝗬 ❌"

𝐒𝐓𝐑𝐈𝐏𝐄 𝐊𝐄𝐘 ⟿ <code>{sk}</code>
𝐒𝐓𝐀𝐓𝐔𝐒 ⟿ {result}

𝐑𝐄𝐐𝐔𝐄𝐒𝐓𝐄𝐃 𝐁𝐘-<a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ]
𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 𝐂𝐇𝐄𝐂𝐊𝐄𝐑 𝐁𝐎𝐓 𝐎𝐅 𝐓𝐄𝐀𝐌 𝐍𝐌𝐁
            </b>"""
                    await Client.edit_message_text(message.chat.id, done.id,
                                                   resp)
                    plancheck = plan_expirychk(user_id)
                    if plancheck == "YES":
                        resp = """
𝐇𝐄𝐘 𝐁𝐎𝐙𝐎𝐎!
𝐏𝐋𝐀𝐍 𝐄𝐗𝐏𝐈𝐑𝐄𝐃 𝐁𝐀𝐁𝐘! 𝐁𝐔𝐘 /buy 𝐨𝐫 𝐁𝐄𝐆 @stripe_xD
            """
                        await Client.send_message(user_id, resp)
                    else:
                        pass
                else:
                    pass

    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")
