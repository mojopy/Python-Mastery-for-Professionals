class UserModel:
    def __init__(self, username="", email=""):
        self.username = username
        self.email = email

    def update_user(self, username, email):
        self.username = username
        self.email = email
