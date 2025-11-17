import asyncio
import logging
import sys
from dotenv import find_dotenv, load_dotenv

from bot import main

if __name__ == "__main__":
    env_path = find_dotenv(".env")
    load_dotenv(env_path)
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
