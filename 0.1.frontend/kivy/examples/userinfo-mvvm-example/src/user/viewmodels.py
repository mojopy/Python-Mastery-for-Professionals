from kivy.properties import StringProperty, ObjectProperty
from kivy.event import EventDispatcher
from user.models import UserModel


class UserViewModel(EventDispatcher):
    def __init__(self):
        self.model = UserModel()

    def load_user(self):
        # Example: Load user data (could be from a database or API)
        self.model.update_user(username="JohnDoe", email="johndoe@example.com")
        self.username = self.model.username
        self.email = self.model.email

    def save_user(self):
        # Save updated data back to the model
        self.model.update_user(self.username, self.email)
        print(f"User saved: {self.username} {self.email}")
        # Here call the api to save user updated data
