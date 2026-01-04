from config import Config
from pyrogram import Client, idle
import asyncio
import logging

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

plugins = dict(root="plugins")

bot = Client(
    "Master",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    sleep_threshold=120,
    plugins=plugins,
    workers=200  # 10000 mat rakho, Render pe heavy hai
)

async def main():
    await bot.start()
    bot_info = await bot.get_me()
    LOGGER.info(f"<--- @{bot_info.username} Started --->")
    await idle()
    await bot.stop()

if __name__ == "__main__":
    asyncio.run(main())


