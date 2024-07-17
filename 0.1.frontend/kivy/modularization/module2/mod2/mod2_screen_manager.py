from kivy.uix.screenmanager import ScreenManager
from mod2.mod2_screen1 import Mod2Screen1
from mod2.mod2_screen2 import Mod2Screen2

class Mod2ScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(Mod2ScreenManager, self).__init__(**kwargs)
        self.add_widget(Mod2Screen1(name='mod2_screen1'))
        self.add_widget(Mod2Screen2(name='mod2_screen2'))
