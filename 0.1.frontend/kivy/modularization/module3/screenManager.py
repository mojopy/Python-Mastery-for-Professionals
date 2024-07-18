# screen_manager.py
from kivy.uix.screenmanager import ScreenManager
from screens.main_screen import MainScreen
from screens.quiz_screen import QuizScreen  # corrected the import to match the class name

class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MainScreen(name='main'))
        self.add_widget(QuizScreen(name='quiz'))
