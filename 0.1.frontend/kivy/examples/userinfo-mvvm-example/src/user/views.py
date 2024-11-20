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
        self.viewmodel = UserViewModel()
        self.viewmodel.load_user()

        self._setup_layout()

    def _setup_layout(self):
        self.layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10
        )

        self.header_label = Label(
            text="User Profile",
            font_size=20
        )

        self.username_input = TextInput(
            text=self.viewmodel.username,
            multiline=False,
            hint_text="Username"
        )
        self.username_input.bind(text=self._update_username)
        
        self.email_input = TextInput(
            text=self.viewmodel.email,
            multiline=False,
            hint_text="Email"
        )
        self.email_input.bind(text=self._update_email)

        self.save_button = Button(text="Save Changes")
        self.save_button.bind(on_press=self._save_user)

        self.user_id_input = TextInput(
            multiline=False, 
            hint_text="Enter User ID",
            size_hint_y=None,
            height=40
        )

        self.get_user_button = Button(
            text="Get User",
            size_hint_y=None,
            height=40
        )
        self.get_user_button.bind(on_press=lambda x: self._get_user(self.user_id_input.text))

        self.add_widget(self.layout)

        self.layout.add_widget(self.header_label)
        self.layout.add_widget(self.username_input)
        self.layout.add_widget(self.email_input)
        self.layout.add_widget(self.save_button)
        self.layout.add_widget(self.user_id_input)
        self.layout.add_widget(self.get_user_button)

    def _update_username(self, instance, value):
        # Update the ViewModel with the new username
        self.viewmodel.username = value

    def _update_email(self, instance, value):
        # Update the ViewModel with the new email
        self.viewmodel.email = value

    def _save_user(self, *args):
        # Trigger the ViewModel's save method
        self.viewmodel.save_user()

    def _get_user(self, id: int):
        self.viewmodel.load_user(id)
        self.username_input.text = self.viewmodel.username
        self.email_input.text = self.viewmodel.email
