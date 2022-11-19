import requests
import json
import dnevniklib.user as user

class Homeworks:
    def __init__(self, session, token, id) -> None:
        self.session = session
        self.token = token
        self.id = id
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
        for activity in data["activities"]:
            if activity["type"] == "LESSON":
                if activity["lesson"]["homework"] != '':
                    lesson_ = activity["lesson"]["subject_name"]
                    homework = activity["lesson"]["homework"]
                    homeworks.append(
                        {str(lesson_): str(homework)}
                    )
        return homeworks