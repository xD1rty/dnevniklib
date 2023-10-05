from requests import get
from dnevniklib.student import Student


class School:
    def __init__(self, student: Student):
        self.token = student.token