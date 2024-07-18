from kivy.uix.screenmanager import ScreenManager
from mod1.mod1_screen1 import Mod1Screen1
from mod1.mod1_screen2 import Mod1Screen2

class Mod1ScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(Mod1ScreenManager, self).__init__(**kwargs)
        mod1_screen1 = Mod1Screen1(name='mod1_screen1')
        mod1_screen2 = Mod1Screen2(name='mod1_screen2')
        self.add_widget(mod1_screen1)
        self.add_widget(mod1_screen2)
