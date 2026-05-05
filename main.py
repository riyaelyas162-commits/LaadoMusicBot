import asyncio
from pyrogram import Client, filters, idle
from pyrogram.types import Message

API_ID = 34871535
API_HASH = "4e38cdb0eb2d2fb20aec1ed339a28c35"
BOT_TOKEN = "8318890496:AAH91pPTBrt10Hxd1g-MXktRNxLVRxCT_nE"

app = Client("music-bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message: Message):
    await message.reply_text("🎵 Music Bot Started Successfully!")

@app.on_message(filters.command("ping"))
async def ping(client, message: Pong):
    await message.reply_text("Pong!")

async def main():
    await app.start()
    print("Bot StaStarted")
    await idle()

if name == "main":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running")

def run_web():
    port = 10000
    server = HTTPServer(("0.0.0.0", port), Handler)
    server.serve_forever()

threading.Thread(target=run_web).start()
