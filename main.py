import os
from pyrogram import Client, filters
from pytgcalls import GroupCallFactory
from pytgcalls.types.input_stream import AudioPiped

API_ID = int(os.getenv("34871535"))
API_HASH = os.getenv("4e38cdb0eb2d2fb20aec1ed339a28c35")
BOT_TOKEN = os.getenv("8318890496:AAGkZKvOOknGLoZrDlxpxzFHyPxMjMqXrZw")
SESSION = os.getenv("SESSION")

bot = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
assistant = Client("assistant", api_id=API_ID, api_hash=API_HASH, session_string=SESSION)

call = GroupCallFactory(assistant).get_group_call()

@bot.on_message(filters.command("start"))
async def start(_, m):
    await m.reply("✅ Bot Working!")

@bot.on_message(filters.command("play") & filters.reply)
async def play(_, m):
    audio = m.reply_to_message.audio or m.reply_to_message.voice
    if not audio:
        return await m.reply("❌ Audio reply karo")

    file = await m.reply_to_message.download()

    await call.join_group_call(
        m.chat.id,
        AudioPiped(file)
    )
    await m.reply("▶️ Playing...")

@bot.on_message(filters.command("stop"))
async def stop(_, m):
    await call.leave_group_call(m.chat.id)
    await m.reply("⏹️ Stopped")

bot.start()
assistant.start()
call.start()

import asyncio
asyncio.get_event_loop().run_forever()
