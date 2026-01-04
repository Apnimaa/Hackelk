import os
import asyncio
from pyrogram import Client

API_ID = int(os.environ["27433400"])
API_HASH = os.environ["+1a286620de5ffe0a7d9b57e604293555"]
BOT_TOKEN = os.environ["8457218709:AAGZpkE5j2YYE0FzoIXxe7d97qSTXcWwVyY"]

bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
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
    





