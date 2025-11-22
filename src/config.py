from os import getenv

from dotenv import find_dotenv, load_dotenv


class Config:
    def __init__(self):
        env_path = find_dotenv(".env")
        load_dotenv(env_path)

        self.BOT_TOKEN = getenv("BOT_TOKEN")
        self.CLIENT_ID = getenv("CLIENT_ID")
        self.CLIENT_SECRET = getenv("CLIENT_SECRET")
        self.AUTH_CODE = getenv("AUTH_CODE")
        self.ACCESS_TOKEN = getenv("ACCESS_TOKEN")
        self.REFRESH_TOKEN = getenv("REFRESH_TOKEN")

        self.__check_refresh_token_exists()

    def __check_refresh_token_exists(self):
        if self.ACCESS_TOKEN is None:
            return

        if self.REFRESH_TOKEN is not None or self.REFRESH_TOKEN != "":
            return

        raise Exception(
            "ACCESS_TOKEN was given without REFRESH_TOKEN needed to update ACCESS_TOKEN every 24hr"
        )
