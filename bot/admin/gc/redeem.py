from FUNC.gc_func import *
from pyrogram import Client, filters
from FUNC.usersdb_func import *
from datetime import date
from datetime import timedelta


@Client.on_message(filters.command("redeem", [".", "/"]))
async def cmd_gc(Client, message):
    #try:
    user_id = str(message.from_user.id)
    regdata = str(getuserinfo(user_id))
    if regdata == 'None':
        resp = "𝐔𝐧𝐫𝐞𝐠𝐢𝐬𝐭𝐞𝐫𝐞𝐝 𝐔𝐬𝐞𝐫. 𝐏𝐫𝐞𝐬𝐬 /register 𝐭𝐨 𝐮𝐬𝐞 𝐦𝐞."
        await message.reply_text(resp, message.id)
    else:
        user_id = str(message.from_user.id)
        msg = message.text.split(" ")
        try:
            gc = msg[1]
        except:
            resp = "❌ 𝗜𝗡𝗩𝗔𝗟𝗜𝗗 𝗚𝗜𝗙𝗧𝗖𝗢𝗗𝗘 ❌"
            await message.reply_text(resp, message.id)
        detail = getgc(gc)
        if str(detail) == 'None':
            resp = "❌ 𝗜𝗡𝗩𝗔𝗟𝗜𝗗 𝗚𝗜𝗙𝗧𝗖𝗢𝗗𝗘 ❌"
            await message.reply_text(resp, message.id)
        else:
            status = detail["status"]
            type = detail["type"]
            if str(status) == "ACTIVE" and str(type) == "PREMIUM":
                time_of_pm = 1
                getpm(user_id,time_of_pm)
                chk = getuserinfo(user_id)
                credit = int(chk["credit"])
                value = credit + 100
                directcredit(user_id, value)
                updategc(gc)
                resp = """✅ 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥 𝐑𝐞𝐝𝐞𝐞𝐦𝐩𝐭𝐢𝐨𝐧. press /credits to get Info
𝗖𝗿𝗲𝗱𝗶𝘁 𝗔𝗱𝗱𝗲𝗱: 𝟭𝟬𝟬 
𝗣𝗹𝗮𝗻: 𝗣𝗿𝗲𝗺𝗶𝘂𝗺
𝐏𝐋𝐀𝐍 𝐕𝐀𝐋𝐈𝐃𝐈𝐓𝐘 ⟿ 𝟭 𝗗𝗮𝘆𝘀"""
                await message.reply_text(resp, message.id)
            elif str(status) == "USED":
                resp = "𝐔𝐬𝐞𝐝 𝐂𝐨𝐝𝐞 𝐋𝐦𝐚𝐨😵‍💫😂"
                await message.reply_text(resp, message.id)
            else:
                resp = "❌ 𝗜𝗡𝗩𝗔𝗟𝗜𝗗 𝗚𝗜𝗙𝗧𝗖𝗢𝗗𝗘 ❌"
                await message.reply_text(resp, message.id)
