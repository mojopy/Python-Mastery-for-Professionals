from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from mod1.mod1_screen_manager import Mod1ScreenManager
from mod2.mod2_screen_manager import Mod2ScreenManager
from mod3.mod3_screen_manager import Mod3ScreenManager

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.sm = ScreenManager()
        mod1_sm = Mod1ScreenManager()
        mod1_sm_screen = Screen(name='mod1')
        mod1_sm_screen.add_widget(mod1_sm)
        
        mod2_sm = Mod2ScreenManager()
        mod2_sm_screen = Screen(name='mod2')
        mod2_sm_screen.add_widget(mod2_sm)
        
        mod3_sm = Mod3ScreenManager()
        mod3_sm_screen = Screen(name='mod3')
        mod3_sm_screen.add_widget(mod3_sm)

        self.sm.add_widget(mod1_sm_screen)
        self.sm.add_widget(mod2_sm_screen)
        self.sm.add_widget(mod3_sm_screen)
        self.add_widget(self.sm)

class HelloApp(App):
    def build(self):
        main_sm = ScreenManager()
        main_screen = MainScreen(name='main')
        main_sm.add_widget(main_screen)
        return main_sm

if __name__ == '__main__':
    HelloApp().run()

