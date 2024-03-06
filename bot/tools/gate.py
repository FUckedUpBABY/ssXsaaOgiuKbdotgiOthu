from pyrogram import Client, filters
import httpx
from FUNC.usersdb_func import *


@Client.on_message(filters.command("gate", [".", "/"]))
async def cmd_gate(Client, message):
    try:
        user_id = str(message.from_user.id)
        chat_type = str(message.chat.type)
        chat_id = str(message.chat.id)
        regdata = str(getuserinfo(user_id))

        if regdata == 'None':
            resp = "𝐔𝐧𝐫𝐞𝐠𝐢𝐬𝐭𝐞𝐫𝐞𝐝 𝐔𝐬𝐞𝐫. 𝐏𝐫𝐞𝐬𝐬 /register 𝐭𝐨 𝐮𝐬𝐞 𝐦𝐞."
            await message.reply_text(resp, quote=True)
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
                resp = "𝐔𝐒𝐄𝐑 𝐍𝐎𝐓 𝐀𝐔𝐓𝐇𝐎𝐑𝐈𝐙𝐄𝐃 𝐓𝐎 𝐔𝐒𝐄 𝐓𝐇𝐈𝐒 𝐂𝐎𝐌𝐌𝐀𝐍𝐃 𝐈𝐍 𝐏𝐄𝐑𝐒𝐎𝐍𝐀𝐋 𝐂𝐇𝐀𝐓."
                await message.reply_text(resp, quote=True)

            elif (chat_type == "ChatType.GROUP" or chat_type == "ChatType.SUPERGROUP") and checkgroup == "None":
                resp = "𝐂𝐇𝐀𝐓 𝐈𝐒 𝐍𝐎𝐓 𝐀𝐔𝐓𝐇𝐎𝐑𝐈𝐙𝐄𝐃 𝐓𝐎 𝐔𝐒𝐄 𝐓𝐇𝐈𝐒 𝐂𝐎𝐌𝐌𝐀𝐍𝐃, 𝐀𝐒𝐊 𝐌𝐘 𝐎𝐖𝐍𝐄𝐑 @stripe_xD ."
                await message.reply_text(resp, quote=True)
            else:

                url = message.text.split(" ", 1)[1]

                async with httpx.AsyncClient() as client:
                    try:
                        response = await client.get(f"https://nivoform.com/gate/gateway.php?url={url}")
                        response.raise_for_status()
                        data = response.json()

                        website_status = data.get('status')
                        captcha = data.get('captcha')
                        cloudflare = data.get('cloudflare')
                        payment_gateways = data.get('gateways')
                        website = data.get('website')

                        if not payment_gateways:
                            payment_gateways = "No gateway Found"

                        resp = f"""<b>
𝐒𝐢𝐭𝐞𝐬 𝐈𝐧𝐟𝐨 ✅
⊶⊶⊶ 
𝐒𝐢𝐭𝐞𝐬 {website}
𝐆𝐚𝐭𝐞𝐬 {payment_gateways}
𝐂𝐚𝐩𝐭𝐜𝐡𝐚 {captcha}
𝐂𝐥𝐨𝐮𝐝𝐟𝐥𝐚𝐫𝐞 {cloudflare}
𝐒𝐢𝐭𝐞 𝐒𝐭𝐚𝐭𝐮𝐬 {website_status}
𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲- @NoMoreBins
</b>
"""
                        await message.reply_text(resp, quote=True)

                    except httpx.HTTPError as http_err:
                        resp = f"<b>Error:</b> HTTP Error: {http_err}"
                        await message.reply_text(resp, quote=True)

                    except Exception as e:
                        resp = f"<b>Error:</b> {e}"
                        await message.reply_text(resp, quote=True)

    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")
