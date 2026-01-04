import os
import asyncio
from pyrogram import Client

# ===== Environment Variables =====
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

if not API_ID or not API_HASH or not BOT_TOKEN:
    raise RuntimeError("API_ID / API_HASH / BOT_TOKEN missing in Render Environment")

API_ID = int(API_ID)

# ===== Pyrogram Client =====
bot = Client(
    name="bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    sleep_threshold=120,
    workers=50
)

# ===== Main =====
async def main():
    await bot.start()
    print("✅ Bot Started Successfully on Render")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
    
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
