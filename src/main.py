import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode

from services.shikimori_client import APIClient
from handlers import routers_list
from config import Config


async def main():
    config = Config()
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(
        token=config.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    await bot.delete_webhook(drop_pending_updates=True)

    dp = Dispatcher()

    api_client = APIClient(
        client_id=config.CLIENT_ID, client_secret=config.CLIENT_SECRET
    )

    dp.include_routers(*routers_list)

    if config.ACCESS_TOKEN:
        api_client.update_tokens(config.ACCESS_TOKEN, config.REFRESH_TOKEN)
    else:
        api_client.authenticate_with_auth_code(config.AUTH_CODE)

    dp["shiki_client"] = api_client
    dp["config"] = config

    # And the run events dispatching
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
