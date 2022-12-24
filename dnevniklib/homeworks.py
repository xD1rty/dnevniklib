import requests
import json
from dnevniklib.errors import *


class Homeworks:
    def __init__(self, user) -> None:
        self.session = user.session
        self.token = user.token
        self.id = user.id

    def get_homeworks_by_data(self, date):
        data = self.session.get(
            f"https://dnevnik.mos.ru/mobile/api/schedule?student_id={self.id}&date={date}",
            headers={
                "Authorization": self.token,
                "Auth-Token": self.token
            }
        ).json()
        homeworks = []
        # print(data)
        try:
            for activity in data["activities"]:
                if activity["type"] == "LESSON":
                    if activity["lesson"]["homework"] != '':
                        lesson_ = activity["lesson"]["subject_name"]
                        homework = activity["lesson"]["homework"]
                        homeworks.append(
                            {
                                "name": str(lesson_),
                                "homework": str(homework)
                            }
                        )
        except KeyError:
            raise DnevnikLibError("Неверная дата")
        return homeworks
