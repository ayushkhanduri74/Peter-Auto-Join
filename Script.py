class script(object):
    START_TXT = """<b>𝙷𝙴𝙻𝙻𝙾 {},
𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href=https://t.me/{}>{}</a>, 𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙴𝙽𝙹𝙾𝚈 😍</b>"""
    
    HELP_TXT = """<𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂.
○ 𝖠𝗏𝖺𝗂𝗅𝖺𝖻𝗅𝖾 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌
     
 /alive - Check I'm Alive..
 /info - User info
 /ping - To get your ping
 /id - User id
 /stats - Db status  
 /broadcast - Broadcast (𝖮𝗐𝗇𝖾𝗋 𝖮𝗇𝗅𝗒)"""


# ⚠️ Please don't change our credits 👇🏻

    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/master793bot>𝗠𝗮𝘀𝘁𝗲𝗿𝟳𝟵𝟯</a>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: KOYEB
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v1.0.1 [ 𝙱𝙴𝚃𝙰 ]"""

    
    MANUELFILTER_TXT = """ʜᴇʟᴘ: <b>ꜰɪʟᴛᴇʀꜱ</b>
- ꜰɪʟᴛᴇʀ ɪꜱ ᴀ ꜰᴇᴀᴛᴜʀᴇ ᴡᴇʀᴇ ᴜꜱᴇʀꜱ ᴄᴀɴ ꜱᴇᴛ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ʀᴇᴘʟɪᴇꜱ ꜰᴏʀ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴋᴇʏᴡᴏʀᴅ ᴀɴᴅ ɪ ᴡɪʟʟ ʀᴇꜱᴘᴏɴᴅ ᴡʜᴇɴᴇᴠᴇʀ ᴀ ᴋᴇʏᴡᴏʀᴅ ɪꜱ ꜰᴏᴜɴᴅ ɪɴ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ
<b>ɴᴏᴛᴇ:</b>
1. ᴛʜɪꜱ ʙᴏᴛ ꜱʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟᴇɢᴇ.
2. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ.
3. ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ ʜᴀᴠᴇ ᴀ ʟɪᴍɪᴛ ᴏꜰ 64 ᴄʜᴀʀᴀᴄᴛᴇʀꜱ.

Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:

• /filter - <code>ᴀᴅᴅ ᴀ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ</code>
• /filters - <code>ʟɪꜱᴛ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴛᴇʀꜱ ᴏꜰ ᴀ ᴄʜᴀᴛ</code>
• /del - <code>ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ</code>
• /delall - <code>ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡʜᴏʟᴇ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ (ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)</code>"""

    BUTTON_TXT = """ʜᴇʟᴘ: <b>ʙᴜᴛᴛᴏɴꜱ</b>
- ᴛʜɪꜱ ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛꜱ ʙᴏᴛʜ ᴜʀʟ ᴀɴᴅ ᴀʟᴇʀᴛ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴꜱ.
<b>ɴᴏᴛᴇ:</b>
1. ᴛᴇʟᴇɢʀᴀᴍ ᴡɪʟʟ ɴᴏᴛ ᴀʟʟᴏᴡꜱ ʏᴏᴜ ᴛᴏ ꜱᴇɴᴅ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴄᴏɴᴛᴇɴᴛ, ꜱᴏ ᴄᴏɴᴛᴇɴᴛ ɪꜱ ᴍᴀɴᴅᴀᴛᴏʀʏ.
2. ᴛʜɪꜱ ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛꜱ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ.
3. ʙᴜᴛᴛᴏɴꜱ ꜱʜᴏᴜʟᴅ ʙᴇ ᴘʀᴏᴘᴇʀʟʏ ᴘᴀʀꜱᴇᴅ ᴀꜱ ᴍᴀʀᴋᴅᴏᴡɴ ꜰᴏʀᴍᴀᴛ
<b>ᴜʀʟ ʙᴜᴛᴛᴏɴꜱ:</b>
<code>[Button Text](buttonurl:https://t.me/master793)</code>
<b>ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ:</b>
<code>[Button Text](buttonalert:ᴛʜɪꜱ ɪꜱ ᴀɴ ᴀʟᴇʀᴛ ᴍᴇꜱꜱᴀɢᴇ)</code>"""

    AUTOFILTER_TXT = """ʜᴇʟᴘ: <b>ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ</b>
<b>ɴᴏᴛᴇ: Fɪʟᴇ Iɴᴅᴇx</b>
1. ᴍᴀᴋᴇ ᴍᴇ ᴛʜᴇ ᴀᴅᴍɪɴ ᴏꜰ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪꜰ ɪᴛ'ꜱ ᴘʀɪᴠᴀᴛᴇ.
2. ᴍᴀᴋᴇ ꜱᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴅᴏᴇꜱ ɴᴏᴛ ᴄᴏɴᴛᴀɪɴꜱ ᴄᴀᴍʀɪᴘꜱ, ᴘᴏʀɴ ᴀɴᴅ ꜰᴀᴋᴇ ꜰɪʟᴇꜱ.
3. ꜰᴏʀᴡᴀʀᴅ ᴛʜᴇ ʟᴀꜱᴛ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴍᴇ ᴡɪᴛʜ Qᴜᴏᴛᴇꜱ. ɪ'ʟʟ ᴀᴅᴅ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇꜱ ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴍʏ ᴅʙ.

<b>Nᴏᴛᴇ: AᴜᴛᴏFɪʟᴛᴇʀ</b>
1. Aᴅᴅ ᴛʜᴇ ʙᴏᴛ ᴀs ᴀᴅᴍɪɴ ᴏɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
2. Usᴇ /connect ᴀɴᴅ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ ᴛʜᴇ ʙᴏᴛ.
3. Usᴇ /settings ᴏɴ ʙᴏᴛ's PM ᴀɴᴅ ᴛᴜʀɴ ᴏɴ AᴜᴛᴏFɪʟᴛᴇʀ ᴏɴ ᴛʜᴇ sᴇᴛᴛɪɴɢs ᴍᴇɴᴜ."""

    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""

    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of 𝙿𝙴𝚃𝙴𝚁

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""

    SONG_TXT = """<b>𝚂𝙾𝙽𝙶 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙼𝙾𝙳𝚄𝙻𝙴</b>

<i>𝚂𝙾𝙽𝙶 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙼𝙾𝙳𝚄𝙻𝙴, 𝙵𝙾𝚁 𝚃𝙷𝙾𝚂𝙴 𝚆𝙷𝙾 𝙻𝙾𝚅𝙴 𝙼𝚄𝚂𝙸𝙲. 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙵𝙴𝙰𝚃𝚄𝙴 𝙵𝙾𝚁 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙰𝙽𝚈 𝚂𝙾𝙽𝙶 𝚆𝙸𝚃𝙷 𝚂𝚄𝙿𝙴𝚁 𝙵𝙰𝚂𝚃 𝚂𝙿𝙴𝙴𝙳.𝚆𝙾𝚁𝙺𝚂 𝙾𝙽𝙻𝚈 𝙾𝙽 𝙶𝚁𝙾𝚄𝙿𝚂../</i>

<b>𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂</b>

⏭️ /song 𝚂𝙾𝙽𝙶 𝙽𝙰𝙼𝙴 

<b>𝚆𝙾𝚁𝙺𝚂 𝙱𝙾𝚃𝙷 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙿𝙼</b>
@MLZ_BOTZ"""

    VIDEO_TXT ="""𝙷𝙴𝙻𝙿 𝚈𝙾𝚄 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝚅𝙸𝙳𝙴𝙾 𝙵𝚁𝙾𝙼 𝚈𝙾𝚄𝚃𝚄𝙱𝙴.
• 𝘜𝘴𝘢𝘨𝘦
𝘠𝘰𝘶 𝘊𝘢𝘯 𝘋𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘈𝘯𝘺 𝘝𝘪𝘥𝘦𝘰 𝘍𝘳𝘰𝘮 𝘠𝘰𝘶𝘵𝘶𝘣𝘦
𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
• 𝘛𝘺𝘱𝘦 /video or /mp4 𝘈𝘯𝘥 (https://youtu.be/example...)
• 𝘌𝘹𝘢𝘮𝘱𝘭𝘦:
<code>/mp4 https://youtu.be/example...</code>
<code>/video https://youtu.be/example...</code>"""

    TTS_TXT = """Help: <b> TTS 🎤 module:</b>
Translate text to speech
<b>Commands and Usage:</b>
• /tts <text> : convert text to speech"""

    GTRANS_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖦𝗈𝗈𝗀𝗅𝖾 𝖳𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾𝗋
𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚝𝚛𝚊𝚗𝚜𝚕𝚊𝚝𝚎 𝚊 𝚝𝚎𝚡𝚝 𝚝𝚘 𝖺𝗇𝗒 𝚕𝚊𝚗𝚐𝚞𝚊𝚐𝚎𝚜 𝚢𝚘𝚞 𝚠𝚊𝚗𝚝. 𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚠𝚘𝚛𝚔𝚜 𝚘𝚗 𝚋𝚘𝚝𝚑 𝚙𝚖 𝚊𝚗𝚍 𝚐𝚛𝚘𝚞𝚙 ✯
➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
➪/tr - 𝖳𝗈 𝗍𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾𝗋 𝗍𝖾𝗑𝗍𝗌 𝗍𝗈 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝖼 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾
➤ 𝖭𝗈𝗍𝖾:
𝖶𝗁𝗂𝗅𝖾 𝗎𝗌𝗂𝗇𝗀 /tr 𝗒𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝗍𝗁𝖾 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾 𝖼𝗈𝖽𝖾
➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾: /𝗍𝗋 𝗆𝗅
• 𝖾𝗇 = 𝖤𝗇𝗀𝗅𝗂𝗌𝗁
• 𝗆𝗅 = 𝖬𝖺𝗅𝖺𝗒𝖺𝗅𝖺𝗆
• 𝗁𝗂 = 𝖧𝗂𝗇𝖽𝗂"""

    TELE_TXT = """<b>▫️HELP: Telegraph▪️</b>
Do as you wish with telegra.ph module!
</b>USAGE:</b>
✒️ /telegraph - Send me Picture or Vide Under (5MB)
<b>NOTE:</b>
• This Command Is Available in goups and pms
• This Command Can be used by everyone"""


    ABOOK_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖠𝗎𝖽𝗂𝗈𝖻𝗈𝗈𝗄
𝚈𝚘𝚞 𝚌𝚊𝚗 𝚌𝚘𝚗𝚟𝚎𝚛𝚝 𝚊 𝙿𝙳𝙵 𝚏𝚒𝚕𝚎 𝚝𝚘 𝚊 𝚊𝚞𝚍𝚒𝚘 𝚏𝚒𝚕𝚎 𝚠𝚒𝚝𝚑 𝚝𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 ✯
➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
➪ /audiobook: 𝖱𝖾𝗉𝗅𝗒 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗍𝗈 𝖺𝗇𝗒 𝖯𝖣𝖥 𝗍𝗈 𝗀𝖾𝗇𝖾𝗋𝖺𝗍𝖾 𝗍𝗁𝖾 𝖺𝗎𝖽𝗂𝗈"""

    DEPLOY_TXT= """𝙸𝙵 𝚈𝙾𝚄 𝙵𝙰𝙲𝙸𝙽𝙶 𝙰𝙽𝚈 𝙸𝚂𝚂𝚄𝙴 𝙸𝙽 𝚃𝙷𝙴 𝚁𝙴𝙿𝙾 𝙲𝙾𝙽𝚃𝙰𝙲𝚃 𝙼𝙴..."""
   
    PINGS_TXT = """<b>Ping Testing:</b>
Helps you to know your ping 🚶🏼‍♂️
<b>Commands:</b>
• /alive - To check you are alive.
• /help - To get help.

• /ping - <b>To get your ping.</b>

<b>🛠️Usage🛠️ :</b>
• This commands can be used in pm and groups
• This commands can be used buy everyone in the groups and bots pm
• Share us for more features"""
 
    STICKER_TXT = """<b>𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙼𝙾𝙳𝚄𝙻𝙴 𝚃𝙾 𝙵𝙸𝙽𝙳 𝙰𝙽𝚈 𝚂𝚃𝙸𝙲𝙺𝙴𝚁𝚂 𝙸𝙳.</b>
• 𝐔𝐒𝐀𝐆𝐄
To Get Sticker ID
 
  ⭕ 𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
 
◉ Reply To Any Sticker [/stickerid]"""

    FONT_TXT= """⚙️ 𝐔𝐒𝐀𝐆𝐄

𝐘𝐎𝐔 𝐂𝐀𝐍 𝐔𝐒𝐄 𝐓𝐇𝐈𝐒 𝐌𝐎𝐃𝐔𝐋𝐄 𝐓𝐎 𝐂𝐇𝐀𝐍𝐆𝐄 𝐅𝐎𝐍𝐓 𝐒𝐓𝐘𝐋𝐄 

<b>COMMAND</b> : /font your text (optional)
        <b> Eg:- /font Hello</b>

 <i>This feature added by @master793"""
    JSON_TXT = """<b>JSON:</b>
Bot returns json for all replied messages with /json or /js
<b>Features:</b>
Message Editting JSON
Pm Support
Group Support
<b>Note:</b>
<b>Everyone can use this command , if spaming happens bot will automatically ban you from the group.</b>"""

    WHOIS_TXT ="""<b>WHOIS MODULE</b>
Note:- <b>Give a user details</b>

•/whois :-give a user full details 📑"""

    URLSHORT_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖴𝗋𝗅 𝗌𝗁𝗈𝗋𝗍𝗇𝖾𝗋
<i><b>𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚜𝚑𝚘𝚛𝚝 𝚊 𝚞𝚛𝚕 </i></b>
➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
➪ /short: <b>𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝗅𝗂𝗇𝗄 𝗍𝗈 𝗀𝖾𝗍 𝗌𝗁𝗈𝗋𝗍𝖾𝖽 𝗅𝗂𝗇𝗄𝗌</b>
➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
<code>/short https://youtu.be/example...</code>"""

    FUN_TXT ="""<b>Gᴀᴍᴇs</b> 
    
<b>⚡ 𝙹𝚄𝚂𝚃 𝚂𝙾𝙼𝙴 𝙺𝙸𝙽𝙳 𝙾𝙵 𝙵𝚄𝙽 𝚃𝙷𝙸𝙽𝙶'𝚂 ⚡</b>
 
𝟣. /dice - 𝚁𝙾𝙻𝙴 𝚃𝙷𝙴 𝙳𝙸𝙲𝙴 
𝟤. /Throw 𝗈𝗋 /Dart - 𝚃𝙾 𝙼𝙰𝙺𝙴 𝙳𝙰𝚁𝚃 
3. /Runs - 𝚂𝙾𝙼𝙴 𝚁𝙰𝙽𝙳𝙾𝙼 𝙳𝙸𝙰𝙻𝙾𝙶𝚄𝙴𝚂 
4. /Goal or /Shoot - 𝚃𝙾 𝙼𝙰𝙺𝙴 𝙰 𝙶𝙾𝙰𝙻 𝙾𝚁 𝚂𝙷𝙾𝙾𝚃
5. /luck or /cownd - 𝚂𝙿𝙸𝙽 𝙰𝙽𝙳 𝚃𝚁𝚈 𝚈𝙾𝚄𝚁 𝙻𝚄𝙲𝙺"""

    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>
• /grp_broadcast - <code>to broadcast a message to all groups</code>
• /gfilter - <code>To add global filter</code>
• /gfilters - <code>To view global filters</code>
• /delallg - <code>To delete all global filters from database</code>
• /delg - <code>To delete a specific global filter</code>
• /setskip - <code>Skip no of files before indexing</code>
• /send - <code>Send any message through bot to users. /send (username/userid) reply with message </code>
• /deletefiles - <code>Delete CamRip and PreDvD files delete from database </code>"""
    
    STATUS_TXT = """<b>★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>

★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>1{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱</b
 """

    CARB_TXT = """<b>Help</b> : 𝗖𝗔𝗥𝗕𝗢𝗡
𝙲𝙰𝚁𝙱𝙾𝙽 𝙸𝚂 𝙰 𝙵𝙴𝚄𝚃𝚄𝚁𝙴 𝚃𝙾 𝙼𝙰𝙺𝙴 𝚃𝙷𝙴 𝙸𝙼𝙰𝙶𝙴 𝙰𝚂 𝚂𝙷𝙾𝚆𝙽 𝙸𝙽 𝚃𝙷𝙴 𝚃𝙾𝙿 𝚆𝙸𝚃𝙷 𝚈𝙾𝚄𝚁𝙴 𝚃𝙴𝚇𝚃𝚂.
𝙵𝙾𝚁 𝚄𝚂𝙸𝙽𝙶 𝚃𝙷𝙴 𝙼𝙾𝙳𝚄𝙻𝙴 𝙹𝚄𝚂𝚃 𝚂𝙴𝙽𝙳 𝚃𝙷𝙴 𝚃𝙴𝚇𝚃 𝙰𝙽𝙳 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙸𝚃 𝚆𝙸𝚃𝙷 /carbon 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝚃𝙷𝙴 𝙱𝙾𝚃 𝚆𝙸𝙻𝙻 𝚁𝙴𝙿𝙻𝚈 𝚆𝙸𝚃𝙷 𝚃𝙷𝙴 𝙲𝙰𝚁𝙱𝙾𝙽 𝙸𝙼𝙰𝙶𝙴"""


    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
    FILE_MSG = """
<b>Hai 👋 {} </b>😍

<b>📫 Your File is Ready</b>

<b>📂 Fɪʟᴇ Nᴀᴍᴇ</b> : <code>{}</code>              
                       
<b>⚙️ Fɪʟᴇ Sɪᴢᴇ</b> : <b>{}</b>
"""
    CHANNEL_CAP = """
<b>Hai 👋 {}</b> 😍

<code>{}</code>

⚠️ <b>This file will be deleted from here within 10 minute as it has copyright ... !!!</b>



<b>© Powered by: <a href=https://t.me/master793>𝗠𝗮𝘀𝘁𝗲𝗿𝟳𝟵𝟯</a></b>
"""
    SUR_TXT = """
<b>
𝙷𝙴𝙻𝙻𝙾 {},
𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href=https://t.me/{}>{}</a>, 𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙴𝙽𝙹𝙾𝚈 
</b>
"""

    IMDB_TEMPLATE_TXT = """
<b>⍞ 𝗧𝗶𝘁𝗹𝗲</b> : <b><i><a href={url}>{title}</a></i></b><b>

⌗ 𝗚𝗲𝗻𝗿𝗲𝘀</b> :<b><i>{genres}</i></b><b>
★ 𝗥𝗮𝘁𝗶𝗻𝗴</b> : <b><i><a href={url}/ratings>{rating}</a> / 10 (ʙᴀsᴇᴅ ᴏɴ {votes} ᴜsᴇʀ ʀᴀᴛɪɴɢ.)</i></b><b>

〄 𝗥𝗲𝗹𝗲𝗮𝘀𝗲𝗱</b> : <b><i>{release_date}</i></b><b>
⌬ 𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲𝘀</b> : <b><i>{languages}</i></b><b>
⛤ 𝗖𝗼𝘂𝗻𝘁𝗿𝗶𝗲𝘀</b> : <b><i>{countries}</i></b><b>
⎙ 𝗦𝘁𝗼𝗿𝘆 𝗟𝗶𝗻𝗲</b> : <code>{plot}</code><b>

★Requested by</b> : {message.from_user.mention}
"""

    CUSTOM_FILE_CAPTION = """📂 <b>File Name</b>: <code>{file_name}</code> 

❤️‍🔥 </b>Join</b> [𝐌𝐀𝐒𝐓𝐄𝐑𝟕𝟗𝟑](https://t.me/master793) """

    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !
📅 Dᴀᴛᴇ : <code>{}</code>
⏰Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code></b>"""

    MELCOW_ENG = """<b>Hᴇʟʟᴏ {} 😍, Aɴᴅ Wᴇʟᴄᴏᴍᴇ Tᴏ {} Gʀᴏᴜᴘ ❤️"""

    ALRT_TXT = """ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏʏ ꜱɪʀ"""

    OLD_ALRT_TXT = """𝐘𝐨𝐮 𝐚𝐫𝐞 𝐮𝐬𝐢𝐧𝐠 𝐨𝐧𝐞 𝐨𝐟 𝐦𝐲 𝐨𝐥𝐝 𝐦𝐞𝐬𝐬𝐚𝐠𝐞𝐬, 𝐩𝐥𝐞𝐚𝐬𝐞 𝐬𝐞𝐧𝐝 𝐭𝐡𝐞 𝐫𝐞𝐪𝐮𝐞𝐬𝐭 𝐚𝐠𝐚𝐢𝐧 """

    TOP_ALRT_MSG = """♻️ ᴄʜᴇᴄᴋɪɴɢ ꜰɪʟᴇ ᴏɴ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ... ♻️"""

    MVE_NT_FND = """<b>ᴛʜɪꜱ ᴍᴏᴠɪᴇ ɪꜱ ɴᴏᴛ ʏᴇᴛ  ʀᴇʟᴇᴀꜱᴇᴅ ᴏʀ ᴀᴅᴅᴇᴅ ᴛᴏ ᴅᴀᴛᴀʙᴀꜱᴇ</b> """

    I_CUDNT = """ʜᴇʟʟᴏ {} ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏ ᴍᴏᴠɪᴇꜱ ɪɴ ᴛʜᴀᴛ ɴᴀᴍᴇ. 
ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ 
➠ ɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ 
➠ ᴛʏᴘᴇ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ 
➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ
➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ 
ᴇxᴀᴍᴘʟᴇ : ᴋᴀɴᴛᴀʀᴀ 2022 
🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ' : ( ! , . / )"""

    I_CUD_NT = """ʜᴇʟʟᴏ {} ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏᴛʜɪɴɢ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴛʜᴀᴛ.ᴄʜᴇᴄᴋ ʏᴏᴜʀ ꜱᴘᴇʟʟɪɴɢ."""
    
    CUDNT_FND = """ʜᴇʟʟᴏ {} ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏᴛʜɪɴɢ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴛʜᴀᴛ ᴅɪᴅ ʏᴏᴜ ᴍᴇᴀɴ ᴀɴʏ ᴏɴᴇ ᴏꜰ ᴛʜᴇꜱᴇ?"""

    REPRT_MSG = """ Join our group ask movies there
    <code>[JOIN GROUP](buttonurl:https://t.me/+1grJbS4HCBswODE1)</code>"""

    CON_TXT = """<b><u>ᴄᴏᴜɴᴛʀʏ ɪɴғᴏ</b></u>
<b>Tʜɪs ᴍᴏᴅᴜʟᴇ ɪs ᴛᴏ ғɪɴᴅ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴄᴏᴜɴᴛʀɪᴇs</b>
• /country [𝖼𝗈𝗎𝗇𝗍𝗋𝗒 𝗇𝖺𝗆𝖾] 
𝖤𝗑𝖺𝗆𝗉𝗅𝖾 :- <code>/country India</code>"""
    UPDATES_TXT = """⍟ Cʜᴀɴɴᴇʟs & Gʀᴏᴜᴘs Mᴏᴅᴜʟᴇ ⍟
🗣️ Bᴏᴛ Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ.

📢 Bᴏᴛ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ."""
    ZOMBIES_TXT = """𝙷𝙴𝙻𝙿 𝚈𝙾𝚄 𝚃𝙾 𝙺𝙸𝙲𝙺 𝚄𝚂𝙴𝚁𝚂
<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>
<b>Commands and Usage:</b>
• /inkick - command with required arguments and i will kick members from group.
• /instatus - to check current status of chat member from group.
• /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
• /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
• /dkick - to kick deleted accounts."""
    
    PIN_TXT ="""<b>PIN MODULE</b>
<b>𝙿𝙸𝙽 𝙰 𝙼𝙴𝚂𝚂𝙰𝙶𝙴../</b>
<b>𝙰𝙻𝙻 𝚃𝙷𝙴 𝙿𝙸𝙽 𝚁𝙴𝙿𝙻𝙰𝚃𝙴𝙳 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙲𝙰𝙽 𝙱𝙴 𝙵𝙾𝚄𝙽𝙳 𝙷𝙴𝚁𝙴::</b>
<b>📌𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴📌</b>
◉ /pin :- 𝚃𝙾 𝙿𝙸𝙽 𝚃𝙷𝙴 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝙾𝙽 𝚈𝙾𝚄𝚁 𝙲𝙷𝙰𝚃𝚂
◉ /unpin :- 𝚃𝙾 𝚄𝙽𝙿𝙸𝙽 𝚃𝙷𝙴 𝙲𝚄𝚁𝚁𝙴𝙴𝙽𝚃 𝙿𝙸𝙽𝙽𝙴𝙳 𝙼𝙴𝚂𝙰𝙰𝙶𝙴"""
    FILE_TXT = """<b>Fɪʟᴇ sᴛᴏʀᴇ ɪs ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴡʜɪᴄʜ ᴡɪʟʟ ᴄʀᴇᴀᴛᴇ ᴀ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ ᴏғ ᴀ sɪɴɢʟᴇ ᴏʀ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</b>

Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
• /batch - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ʙᴀᴛᴄʜ ʟɪɴᴋ ᴏғ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</code>
• /link - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ sɪɴɢʟᴇ ғɪʟᴇ sᴛᴏʀᴇ ʟɪɴᴋ.</code>
• /pbatch - <code>Jᴜsᴛ ʟɪᴋᴇ /batch, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇs ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴs.</code>
• /plink - <code>Jᴜsᴛ ʟɪᴋᴇ /link, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇ ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴ.</code>"""
    NORSLTS = """
★ #𝗡𝗼𝗥𝗲𝘀𝘂𝗹𝘁𝘀 ★

𝗜𝗗 <b>: {}</b>

𝗡𝗮𝗺𝗲 <b>: {}</b>

𝗠𝗲𝘀𝘀𝗮𝗴𝗲 <b>: {}</b>"""







