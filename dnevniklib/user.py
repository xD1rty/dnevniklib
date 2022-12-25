from requests import Session
from dnevniklib.errors import DnevnikLibError


class User:
    def __init__(self, token=None) -> None:
        # Init function
        self.default_api_url = "https://dnevnik.mos.ru/mobile/api"
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
            self.contract_id = self.data_about_user["children"][0]["contract_id"]
            self.parents = self.data_about_user["children"][0]["representatives"]
        else:
            if self.data_about_user == 403:
                raise DnevnikLibError("non-existent token")
            elif self.data_about_user == 400:
                raise DnevnikLibError("Bad Request")
            elif self.data_about_user == 402:
                raise DnevnikLibError("Non-existent token")
            elif self.data_about_user == 401:
                raise DnevnikLibError("Your token expired")
            else:
                raise DnevnikLibError()


    def login(self):
        """
        Сюда ничего не задаем
        :return:
        """
        result = self.session.get(
            f"{self.default_api_url}/profile",
            headers={
                "Authorization": self.token,
                "Auth-Token": self.token
                })
        if result.status_code != 200:
            return [0, result.status_code]
        
        if result.json():
            return [result.json(), result.status_code]

    def get_date_in_format(self, year, month, day) -> str:
        """

        :param year:
        :param month:
        :param day:
        :return:
        """
        if len(str(day)) == 1:
            date ="0"+str(day)
        if len(str(month)) == 1:
            month ="0"+str(month)
        return f"{year}-{month}-{day}"

    def get_attendance_by_date(self, to_date, from_date):
        """
        :param to_date:
        :param from_date:
        :param contract_id:
        :return:
        """
        data = self.session.get(
            f"{self.default_api_url}/visits?from={from_date}&to={to_date}&contract_id={self.contract_id}",
            headers={
                "Authorization": self.token,
                "Auth-Token": self.token
            }
        )
        return data.json()["payload"]
    def get_notifications(self):
        """

        :return:
        """
        return self.session.get(
            f"{self.default_api_url}/notifications/search?student_id={self.id}",
            headers={
                "Authorization": self.token,
                "Auth-Token": self.token
            }
        ).json()
        
