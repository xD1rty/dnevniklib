from requests import get
from dnevniklib.errors import DnevnikTokenError


class Student:
    def __init__(self, token):
        self.token = token
        self.userinfo = get("https://school.mos.ru/v3/userinfo", headers={
            "Authorization": f"Bearer {self.token}"
        })
        self.student_profile_data = get(
            "https://dnevnik.mos.ru/core/api/student_profiles/",
            headers={
                "Auth-Token": token
            }
        )
        if self.student_profile_data.status_code != 200 or self.userinfo.status_code != 200:
            raise DnevnikTokenError(self.token)
        self.id = self.student_profile_data.json()[0]["id"]
        self.first_name = self.userinfo.json()["info"]["FirstName"]
        self.middle_name = self.userinfo.json()["info"]["MiddleName"]
        self.last_name = self.userinfo.json()["info"]["LastName"]
        self.birthdate = self.userinfo.json()["info"]["birthdate"]
        self.email = self.userinfo.json()["info"]["mail"]
        self.person_id = self.student_profile_data.json()[0]["person_id"]
        self.school_id = self.student_profile_data.json()[0]["school_id"]
        self.age = self.student_profile_data.json()[0]["age"]
        self.sex = self.student_profile_data.json()[0]["sex"]
        self.login = self.student_profile_data.json()[0]["gusoev_login"]
        self.class_name = self.student_profile_data.json()[0]["class_unit"]["name"]
