from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


from shikimori_client import APIClient
from config import Config

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    start_text = "Привет, я бот который работает при помощи [Shikimori](https://shikimori.one/)! Для получения доступа ко всем командам напиши /help"
    """
    This handler receives messages with `/start` command
    """
    await message.answer(
        start_text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True
    )


@dp.message(Command("help"))
async def command_help_handler(message: Message) -> None:
    await message.answer("Плейсхолдер для команды /help")


@dp.message(Command("about"))
async def command_about_handler(message: Message) -> None:
    about_text = "Сделано на базе API [Shikimori](https://shikimori.one/), большое спасибо за доступ к API!\nСоздатель: @rosentur\nGithub: https://github.com/MeowRosya"
    await message.answer(
        about_text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True
    )


@dp.message(Command("test"))
async def command_test_handler(message: Message, shiki_client: APIClient) -> None:
    await message.answer(shiki_client.get_anime("test"))


@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(
        token=Config.bot_token(),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    await bot.delete_webhook(drop_pending_updates=True)

    api_client = APIClient(
        client_id=Config.client_id(), client_secret=Config.client_secret()
    )

    if Config.access_token():
        api_client.add_access_token(Config.access_token())
    else:
        api_client.authenticate_with_auth_code(Config.auth_code())

    dp["shiki_client"] = api_client

    # And the run events dispatching
    await dp.start_polling(bot)
