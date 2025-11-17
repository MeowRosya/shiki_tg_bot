from os import getenv


class Config:
    @classmethod
    def bot_token(cls):
        return getenv("BOT_TOKEN")

    @classmethod
    def client_id(cls):
        return getenv("CLIENT_ID")

    @classmethod
    def client_secret(cls):
        return getenv("CLIENT_SECRET")

    @classmethod
    def auth_code(cls):
        return getenv("AUTH_CODE")

    @classmethod
    def access_token(cls):
        return getenv("ACCESS_TOKEN")
