# (c) @RoyalKrrishna

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is Maxx Search Bot.

My Name: <a href='https://t.me/maxxmoviesrobot'>Maxx Movies Robot</a>

Language : <a href='https://www.python.org'> Python V3</a>

Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

Server: <a href='https://heroku.com'>Private</a>

Created By: <a href='https://t.me/botfather'>Dont Click</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Developer : <a href='https://t.me/Royaldwip'>Private</a>

ɪ Aᴍ Sɪᴍᴘʟᴇ Mᴏᴠɪᴇ Fɪɴᴅɪɴɢ Rᴏʙᴏᴛ.. 
Iғ Yᴏᴜ Dᴏɴ'ᴛ Kɴᴏᴡ Hᴏᴡ Tᴏ Usᴇ Mᴇ? 
Kᴏɪ Nᴀ Bᴀᴛᴀ Dᴇᴛʜᴀ Hᴏᴏɴ Mᴜᴊᴇ Kᴀɪsᴀ Usᴇ Kᴀʀᴇ! Wᴀsᴀ Yᴇ Mᴀᴛ Sᴀᴍᴊᴏ Mᴜᴊᴇ Eɴɢʟɪsʜ Nʜɪ Aᴛᴀ Hᴀɪɴ Mᴜᴊᴇ Aᴛᴀ Hᴀɪɴ Bᴜᴛ Bᴏʟᴛᴀ Nʜɪ Bᴇᴄᴀᴜsᴇ Eɴɢʟɪsʜ Iɴᴅɪᴀ Kᴀ Lᴀɴɢᴜᴀɢᴇ Nʜɪ HᴀɪN.. 
Bᴜᴛ Fʜɪʀ Bʜɪ Bᴏʟᴛᴀ Hᴏᴏɴ Kʏᴀ Kᴀʀᴇ Bᴀᴄʜᴘᴀɴ Sᴇ Sɪᴋʜɴᴀ Pᴀʀᴀ Nʜɪ Tᴏʜ Sɪʀ Eɴɢʟɪsʜ Pᴀʀ Mᴀʀᴋs Kᴀᴍ Kᴀʀ Dᴇᴛʜᴀ Hᴀɪɴ 🤣\n\nBᴇ Sᴇʀɪᴏᴜs Oᴋᴀʏ.. \n\nHᴀɴ Tᴏʜ Mᴜᴊᴇ Bᴀs Mᴏᴠɪᴇ Kᴀ Nᴀᴍ Lɪᴋʜᴇ Dᴏ Mᴇ Aᴘᴋɪ Jᴀʀᴏʀᴀᴛ Kɪ Mᴏᴠɪᴇ Kᴀ Lɪɴᴋ Dᴜɴɢᴀ Bᴜᴛ Cᴏɴᴅɪᴛɪᴏɴ Hᴀɪɴ Aᴘ Mᴜᴊᴇ Gᴀʟᴀᴛ Sᴘᴇʟʟɪɴɢ Nʜɪ Dᴇ Sᴀᴋᴛᴇ Nʜɪ Tᴏʜ Mᴇ Aᴘᴋᴏ Mᴏᴠɪᴇ Nʜɪ Dᴇ Pᴀʏᴏɴɢᴀ Oᴋᴀʏ.. \n\nAᴜʀ Eᴋ Bᴀᴛ Aɢᴀʀ Mᴏᴠɪᴇ Mᴇʀᴇ Dᴀᴛᴀʙᴀsᴇ Pᴀʀ Nʜɪ Hᴀɪɴ Tᴏ Aᴘ Mᴇʀᴇ Oᴡɴᴇʀ Kᴏ Bᴏʟ Sᴀᴋᴛᴇ Hᴏᴏɴ Wᴏʜ Dᴀʟ Dᴇɢᴀ.. @Dreamer999\n\n🔴 Nᴏᴛᴇ :(
(Pʜᴇʟᴇ Gᴏᴏɢʟᴇ Pᴇ Jᴀᴋᴇ Sᴘᴇʟʟɪɴɢ Cʜᴇᴋ Kᴀʀɴᴀ Fʜɪʀ Oᴡɴᴇʀ Kᴏ Bᴏʟɴᴀ Nʜɪ Tᴏ Bʟᴏᴄᴋ Bʜɪ Kᴀʀ Sᴀᴋᴛᴀ Hᴀɪɴ).</b>
"""

    HOME_TEXT = """
<b>Hello! {} 🙏,

I'm Maxx Search Robot</a>

I Can Search Movies What You Want

<a>For Any Query @Dreamer999</a></b>
"""


    START_MSG = """
<b>Hello! {} 🙏,

I'm Maxx Search Robot</a>

I Can Search Movies What You Want

<a>For Any Query @Dreamer999</a></b>
"""


