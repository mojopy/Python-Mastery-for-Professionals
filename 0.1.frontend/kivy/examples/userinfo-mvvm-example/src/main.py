from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from user.views import HomeScreen


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="home"))
        return sm


if __name__ == "__main__":
    MyApp().run()
