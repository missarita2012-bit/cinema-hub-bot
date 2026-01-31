from pyrogram import Client, filters

# ====== YAHIN FILL KARO ======
API_ID = 123456          # ← apna API_ID
API_HASH = "API_HASH_HERE"
BOT_TOKEN = "BOT_TOKEN_HERE"

STREAM_SITE = "https://streamer-1cvs.onrender.com"
# ============================

app = Client(
    "cinema_hub_link_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "🎬 Movie / video bhejo ya forward karo.\n"
        "Main streaming link de dunga."
    )

@app.on_message(filters.video | filters.document)
async def give_link(client, message):
    file_id = message.video.file_id if message.video else message.document.file_id
    link = f"{STREAM_SITE}/watch/{file_id}"

    await message.reply_text(
        f"🎬 Streaming Link Ready\n\n{link}",
        disable_web_page_preview=True
    )

app.run()