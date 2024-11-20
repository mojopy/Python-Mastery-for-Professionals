from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from user.viewmodels import UserViewModel


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Initialize the ViewModel
        self.vm = UserViewModel()
        self.vm.load_user()

        # Create the layout
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=10)
        self.add_widget(self.layout)

        # Bind UI elements to the ViewModel properties
        self.layout.add_widget(Label(text="User Profile", font_size=20))

        self.username_input = TextInput(
            text=self.vm.username, multiline=False, hint_text="Username"
        )
        self.username_input.bind(text=self.update_username)
        self.layout.add_widget(self.username_input)

        self.email_input = TextInput(
            text=self.vm.email, multiline=False, hint_text="Email"
        )
        self.email_input.bind(text=self.update_email)
        self.layout.add_widget(self.email_input)

        save_button = Button(text="Save Changes")
        save_button.bind(on_press=self.save_user)
        self.layout.add_widget(save_button)

    def update_username(self, instance, value):
        # Update the ViewModel with the new username
        self.vm.username = value

    def update_email(self, instance, value):
        # Update the ViewModel with the new email
        self.vm.email = value

    def save_user(self, *args):
        # Trigger the ViewModel's save method
        self.vm.save_user()
