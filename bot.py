# (c) HeimanPictures

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
from config import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "PDiskBot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )
    app.run()
@bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(
        f"**𝗛𝗘𝗟𝗟𝗢🎈{message.chat.first_name}!**\n\n"
        "𝐈'𝐦 𝐚 𝐏𝐝𝐢𝐬𝐤 𝐔𝐩𝐥𝐨𝐚𝐝𝐞𝐫 𝐛𝐨𝐭. 𝐉𝐮𝐬𝐭 𝐬𝐞𝐧𝐝 𝐦𝐞 𝐥𝐢𝐧𝐤 𝐨𝐫 𝐅𝐮𝐥𝐥 𝐩𝐨𝐬𝐭... \n 𝐓𝐡𝐢𝐬 𝐛𝐨𝐭 𝐢𝐬 𝐦𝐚𝐝𝐞 𝐛𝐲 @ParitoshPky_Official💖")
