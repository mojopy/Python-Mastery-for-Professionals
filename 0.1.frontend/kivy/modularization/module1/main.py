from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.main_screen import MainScreen
from screens.quiz_screen import QuizScreen

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(QuizScreen(name='quiz'))
        return sm

if __name__ == '__main__':
    MyApp().run()

