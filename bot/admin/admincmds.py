from pyrogram import Client, filters

@Client.on_message(filters.command("adm", [".", "/"]))
async def cmd_adm(Client, message):
    try:
        user_id = str(message.from_user.id)
        CEO = "5371579102"
        if user_id != CEO:
            resp = "𝙈𝙛 𝙔𝙤𝙪 𝙖𝙧𝙚 𝙉𝙤𝙩 𝙩𝙝𝙚 𝙊𝙬𝙣𝙚𝙧"
            msg1 = await message.reply_text(resp, message.id)
        else:
            resp = f"""
𝐓𝐄𝐀𝐌 𝐍𝐎𝐌𝐎𝐑𝐄𝐁𝐈𝐍𝐒 𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 𝐁𝐎𝐓 𝗔𝗗𝗠𝗜𝗡 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦

𝐆𝐑𝐎𝐔𝐏 𝐀𝐔𝐓𝐇𝐎𝐑𝐈𝐙𝐀𝐓𝐈𝐎𝐍
<code>/add -100765464554</code>
𝐆𝐑𝐎𝐔𝐏 𝐃𝐄-𝐀𝐔𝐓𝐇𝐎𝐑𝐈𝐙𝐀𝐓𝐈𝐎𝐍
<code>/del -10098796668</code>
𝐆𝐑𝐎𝐔𝐏 𝐌𝐄𝐌𝐁𝐄𝐑 𝐏𝐑𝐎𝐌𝐎𝐓𝐄
<code>/pm 1386450737</code>
𝐆𝐑𝐎𝐔𝐏 𝐌𝐄𝐌𝐁𝐄𝐑 𝐃𝐄𝐌𝐎𝐓𝐄
<code>/fr 1386450737</code>
𝐒𝐓𝐀𝐑𝐓𝐄𝐑 𝐏𝐋𝐀𝐍 𝐆𝐈𝐅𝐓
<code>/plan1 1386450737</code>
𝐒𝐈𝐋𝐕𝐄𝐑 𝐏𝐋𝐀𝐍 𝐆𝐈𝐅𝐓
<code>/plan2 1386450737</code>
𝐆𝐎𝐋𝐃 𝐏𝐋𝐀𝐍 𝐆𝐈𝐅𝐓
<code>/plan3 1386450737</code>
𝐂𝐔𝐒𝐓𝐎𝐌 𝐔𝐒𝐄𝐑 𝐏𝐋𝐀𝐍
<code>/cs 1386450737</code>
𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐆𝐂 𝐆𝐄𝐍
<code>/pmgc 10</code>
𝐒𝐓𝐀𝐑𝐓𝐄𝐑 𝐆𝐂 𝐆𝐄𝐍
<code>/stgc 10</code>
𝐒𝐈𝐋𝐕𝐄𝐑 𝐆𝐂 𝐆𝐄𝐍
<code>/slgc 10</code>
𝐆𝐎𝐋𝐃 𝐆𝐂 𝐆𝐄𝐍
<code>/gldgc 10</code>
𝐆𝐑𝐎𝐔𝐏 𝐌𝐄𝐌𝐁𝐄𝐑 𝐂𝐑𝐄𝐃𝐈𝐓 𝐀𝐃𝐃
<code>/ac 100 1386450737</code>
𝐁𝐑𝐎𝐃𝐂𝐀𝐒𝐓
<code>/brd message</code>
      """
            await message.reply_text(resp, message.id)
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")
