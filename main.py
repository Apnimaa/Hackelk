from pyrogram import Client
import asyncio

API_ID = int(os.environ.get("27433400"))
API_HASH = os.environ.get("1a286620de5ffe0a7d9b57e604293555")
BOT_TOKEN = os.environ.get("8457218709:AAGZpkE5j2YYE0FzoIXxe7d97qSTXcWwVyY")
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
    



