import os
import asyncio
from pyrogram import Client

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = Client(
    "bot",
    api_id=27433400,
    api_hash="1a286620de5ffe0a7d9b57e604293555",
    bot_token="8457218709:AAGZpkE5j2YYE0FzoIXxe7d97qSTXcWwVyY",
    sleep_threshold=120,
    plugins=plugins,
    workers=200,
)

async def main():
    await bot.start()
    print("Bot Started Successfully")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
    







