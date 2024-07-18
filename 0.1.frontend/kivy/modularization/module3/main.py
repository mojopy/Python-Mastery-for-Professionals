# main.py (your main application file)
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.main_screen import MainScreen
from screens.quiz_screen import QuizScreen
#from screenManager import MyScreenManager


class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)

        self.add_widget(MainScreen(name='main'))
        self.add_widget(QuizScreen(name='quiz'))
        
class MyApp(App):
    def build(self):
        return MyScreenManager()
    
if __name__ == '__main__':
    MyApp().run()
