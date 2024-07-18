from kivy.uix.screenmanager import ScreenManager
from mod3.mod3_screen1 import Mod3Screen1
from mod3.mod3_screen2 import Mod3Screen2

class Mod3ScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(Mod3ScreenManager, self).__init__(**kwargs)
        mod3_screen1 = Mod3Screen1(name='mod3_screen1')
        mod3_screen2 = Mod3Screen2(name='mod3_screen2')
        self.add_widget(mod3_screen1)
        self.add_widget(mod3_screen2)
