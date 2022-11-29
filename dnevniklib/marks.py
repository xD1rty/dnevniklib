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
    def get_trimester_marks(self, trimester: int, academic_year_id: int = 10):
        """
        Триместр вводим в последовательности 0 - 1 триместр, 1 - 2 триместр, 2 - 3 триместр
        ID года вводим 10
        """
        data = self.session.get(
            f"https://dnevnik.mos.ru/reports/api/progress/json?academic_year_id={academic_year_id}&student_profile_id={self.id}",
            headers={
                "Authorization": self.token,
                "Auth-Token": self.token
            }
        ).json()
        marks = []
        for lesson in data:
            lesson_name = lesson["subject_name"]
            if lesson["periods"] != []:
                trimester_mark = lesson["periods"][0]["avg_five"]
            else:
                trimester_mark = "0"
            marks.append({lesson_name: trimester_mark})
        return marks





