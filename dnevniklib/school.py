class School:
    def __init__(self, session, token, data_about_user) -> None:
        self.session = session
        self.token = token
        self.data_about_user = data_about_user
    def get_info_about_school(self):

        # print(data)
        return self.data_about_user["children"][0]["school"]