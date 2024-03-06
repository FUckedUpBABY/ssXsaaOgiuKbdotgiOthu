from FUNC.gc_func import *
from pyrogram import Client, filters


@Client.on_message(filters.command("gc", [".", "/"]))
async def cmd_gc(client, message):
    try:
        user_id = str(message.from_user.id)
        CEO = "5371579102"
        if user_id != CEO:
            resp = "𝙈𝙛 𝙔𝙤𝙪 𝙖𝙧𝙚 𝙉𝙤𝙩 𝙩𝙝𝙚 𝙊𝙬𝙣𝙚𝙧"
            await message.reply_text(resp, message.id)
        else:
            msg = message.text.split(" ")
            try:
                gen_amt = msg[1]
            except:
                gen_amt = ""
            if len(gen_amt) == 0:
                amt = 10
            else:
                amt = int(gen_amt)
            text = f"""𝐆𝐢𝐟𝐭𝐜𝐨𝐝𝐞 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐟𝐮𝐥𝐥 ✅
𝐀𝐌𝐎𝐔𝐍𝐓 ⊶ {amt}\n"""
            for i in range(amt):
                GC = f"NMB-{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
                insert_pm(GC)
                text += f"""
<code>{GC}</code>
𝐕𝐀𝐋𝐔𝐄 ⊶ 𝟭𝟬𝟬 𝗖𝗿𝗲𝗱𝗶𝘁𝘀 + 𝗣𝗿𝗲𝗺𝗶𝘂𝗺\n"""

            text += f"""
𝐇𝐎𝐖 𝐓𝐎 𝐑𝐄𝐃𝐄𝐄𝐌? 
𝗧𝘆𝗽𝗲 /redeem"""
            send = await message.reply_text(text, message.id)
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")
