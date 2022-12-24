class School:
    def __init__(self, user) -> None:
        self.session = user.session
        self.token = user.token
        self.data_about_user = user.data_about_user
    def get_info_about_school(self):

        # print(data)
        return self.data_about_user["children"][0]["school"]