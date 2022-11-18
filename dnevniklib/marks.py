import requests
import json 

class Marks:
    def __init__(self, session, token, id) -> None:
        self.session = session
        self.token = token
        self.id = id
    def get_marks_by_data(self, date):
        data = self.session.get(
            f"https://dnevnik.mos.ru/mobile/api/schedule?student_id={self.id}&date={date}",
            headers={
                "Authorization": self.token,
                "Auth-Token": self.token
            }
        ).json()
        marks = []
        # print(data)
        for activity in data["activities"]:
            if activity["type"] == "LESSON":
                if activity["lesson"]["marks"] != []:
                    lesson_ = activity["lesson"]["subject_name"]
                    mark = activity["lesson"]["marks"][0]["value"]
                    marks.append(
                        {str(lesson_): str(mark)}
                    )
        return marks



