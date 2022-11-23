from requests import Session
from dnevniklib.errors import DnevnikLibError
class User:
    def __init__(self, token=None) -> None:
        # Init function
        self.token = token
        self.session = Session()
        self.data_about_user = self.login()
        if self.data_about_user[1] == 200:
            self.data_about_user = self.data_about_user[0]
            self.first_name = self.data_about_user["profile"]["first_name"]
            self.last_name = self.data_about_user["profile"]["last_name"]
            self.middle_name = self.data_about_user["profile"]["middle_name"]
            self.type = self.data_about_user["profile"]["type"]
            self.id = self.data_about_user["profile"]["id"]
            self.phone = self.data_about_user["profile"]["phone"]
            self.email = self.data_about_user["profile"]["email"]
            self.birth_date = self.data_about_user["children"][0]["birth_date"]
            self.sex = self.data_about_user["children"][0]["sex"]
            self.class_name = self.data_about_user["children"][0]["class_name"]
        else:
            if self.data_about_user == 403:
                raise DnevnikLibError("non-existent token")
            elif self.data_about_user == 400:
                raise DnevnikLibError("Bad Request")
            else:
                raise DnevnikLibError("Not Found")


    def login(self) -> str:
        result = self.session.get(
            "https://dnevnik.mos.ru/mobile/api/profile", 
            headers={
                "Authorization": self.token,
                "Auth-Token": self.token
                })
        print(result.status_code)
        if result.status_code != 200:
            return [0, result.status_code]
        
        if result.json():
            return [result.json(), result.status_code]

    def get_date_in_format(self, year, month, date):
        return f"{year}-{month}-{date}" 
        