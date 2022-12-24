class Lessons:
    def __init__(self, user) -> None:
        self.data = user.data_about_user
    
    def get_lessons(self):
        return self.data_about_user["children"][0]["groups"]
    def get_sections(self):
        return self.data_about_user["children"][0]["sections"]