import os
from pyrogram import Client, filters
from pyrogram.types import Message
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

API_ID = 34871535
API_HASH = "4e38cdb0eb2d2fb20aec1ed339a28c35"
BOT_TOKEN = "8318890496:AAGkZKvOOknGLoZrDlxpxzFHyPxMjMqXrZw"

app = Client(
    "music-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(client, message: Message):
    await message.reply_text("🎵 Bot successfully chal raha hai!")

@app.on_message(filters.command("ping"))
async def ping(client, message: Message):
    await message.reply_text("🏓 Pong!")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running")

def run_web():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), Handler)
    server.serve_forever()

threading.Thread(target=run_web, daemon=True).start()

print("Bot start ho raha hai...")

app.run()
