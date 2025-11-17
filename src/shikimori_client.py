import requests


class APIClient:
    def __init__(self, client_id: str, client_secret: str) -> None:
        self.access_token = None
        self.refresh_token = None
        self.client_id = client_id
        self.client_secret = client_secret

    def authenticate_with_auth_code(self, auth_code: str) -> None:
        """
        Used when get first auth code. When already user auth code once need to refresh it
        """
        url = "https://shikimori.one/oauth/token"

        headers = {"User-Agent": "RosenthurApp"}

        data = {
            "grant_type": "authorization_code",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "code": auth_code,
            "redirect_uri": "urn:ietf:wg:oauth:2.0:oob",
        }

        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()  # Выбросит исключение для статусов 4xx/5xx

        res = dict(response.json())
        self.access_token = res["access_token"]

        print(f"Get access token: {self.access_token}")

    def add_access_token(self, access_token) -> None:
        """
        Used when access token already exists
        """
        self.access_token = access_token

    def get_anime(self, anime_title: str):
        url = "https://shikimori.one/api/graphql"

        headers = {
            "User-Agent": "RosenthurApp",
            "Authorization": f"Bearer {self.access_token}",
        }

        data = '"query":"{\n animes(search: "bakemono", limit: 1, kind: "!special")\n {id}"'

        response = requests.get(url, headers=headers, data=data)
        response.raise_for_status()  # Выбросит исключение для статусов 4xx/5xx

        res = dict(response.json())
        return str(res)

    def _refresh_token(self) -> str: ...
