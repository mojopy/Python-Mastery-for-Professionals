from kivy.properties import StringProperty, ObjectProperty
from kivy.event import EventDispatcher
from user.models import UserModel
import requests


API_BASE_URL = "http://localhost:8000"

class UserViewModel(EventDispatcher):
    username = StringProperty("")
    email = StringProperty("")

    def __init__(self):
        super().__init__()
        self.model = UserModel()

    def load_user(self, user_id=0):
        response = requests.get(f"{API_BASE_URL}/user/{user_id}")
        if response.status_code == 200:
            user_data = response.json()
            self.model = UserModel(**user_data)
            self.username = self.model.username
            self.email = self.model.email

    def save_user(self):
        self.model = UserModel(username=self.username, email=self.email)
        response = requests.post(f"{API_BASE_URL}/user", json=self.model.to_dict)
        if response.status_code == 200:
            print(f"User saved successfully: {self.username} {self.email}")

    def get_user(self, id: int):
        response = requests.get(f"{API_BASE_URL}/user/{id}")
        if response.status_code == 200:
            user_data = response.json()
            print(user_data)
