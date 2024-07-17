from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from mod1.mod1_screen_manager import Mod1ScreenManager
from mod2.mod2_screen_manager import Mod2ScreenManager
from mod3.mod3_screen_manager import Mod3ScreenManager

class MainScreenManager(ScreenManager):
    pass

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.sm = MainScreenManager()
        self.sm.add_widget(Mod1ScreenManager(name='mod1'))
        self.sm.add_widget(Mod2ScreenManager(name='mod2'))
        self.sm.add_widget(Mod3ScreenManager(name='mod3'))
        self.add_widget(self.sm)

class HelloApp(App):
    def build(self):
        main_sm = ScreenManager()
        main_sm.add_widget(MainScreen(name='main'))
        return main_sm

if __name__ == '__main__':
    HelloApp().run()