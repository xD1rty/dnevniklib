from requests import Session

class User:
    def __init__(self, login=None, password=None, token=None) -> None:
        # Init function
        self.username = login
        self.password = password
        self.token = token
        self.session = Session()
        self.first_name = None
        self.last_name = None
        self.type = None
        self.id = None

    def login(self) -> str:
        return self.login_by_token()
    
    def login_by_token(self) -> str:
        result = self.session.get(
            "https://dnevnik.mos.ru/mobile/api/profile", 
            headers={
                "Authorization": self.token,
                "Auth-Token": self.token
                }).json()
        self.first_name = result["profile"]["first_name"]
        self.last_name = result["profile"]["last_name"]
        self.type = result["profile"]["type"]
        self.id = result["profile"]["id"]
        return result