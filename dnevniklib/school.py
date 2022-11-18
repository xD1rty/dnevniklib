import requests
import user

class School:
    def __init__(self, session, token) -> None:
        self.session = session
        self.token = token
        
    def get_info_about_school(self):
        data = self.session.get(
            "https://dnevnik.mos.ru/mobile/api/profile",
            headers={
                "Authorization": self.token,
                "Auth-Token": self.token
            }
        ).json()
        # print(data)
        return data["children"][0]["school"]