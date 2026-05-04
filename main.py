from pyrogram import Client, filters
from pyrogram.types import Message

API_ID = int("34871535")
API_HASH = "4e38cdb0eb2d2fb20aec1ed339a28c35"
BOT_TOKEN = "8318890496:AAF1CN_dyMIXTe7Nexf_HMEElJ>"

app = Client("music-bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
def start(client, message: Message):
    message.reply_text("🎵 Music Bot Started Successfully!")

@app.on_message(filters.command("ping"))
def ping(client, message: Message):
    message.reply_text("🏓 Pong!")

app.run()