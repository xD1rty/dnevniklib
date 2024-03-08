from dnevniklib.student import Student
from requests import get
from dnevniklib.types import Homework as HomeworkType


class Homeworks:
    def __init__(self, student: Student):
        self.student = student

    def get_homework_by_date(self, date):
        res = []
        response = get(
            f"https://school.mos.ru/api/family/web/v1/homeworks?from={date}&to={date}&student_id={self.student.id}",
            headers={
                "Auth-Token": self.student.token,
                "X-Mes-Subsystem": "familyweb"
            }
        )
        for homework in response.json()["payload"]:
            res.append(
                HomeworkType(
                    id=homework["homework_entry_student_id"],
                    description=homework["description"],
                    subject_id=homework["subject_id"],
                    subject_name=homework["subject_name"],
                    created_at=homework["date_assigned_on"],
                    is_done=homework["is_done"]
                )
            )
        return res