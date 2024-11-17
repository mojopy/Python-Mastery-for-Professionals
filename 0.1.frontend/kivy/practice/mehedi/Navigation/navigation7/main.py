from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, CardTransition

class HomeScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class MyApp(App):
    def build(self):
        sm = ScreenManager(transition=CardTransition(direction='left', mode='push'))
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(SettingsScreen(name='settings'))
        return sm

if __name__ == '__main__':
    MyApp().run()
