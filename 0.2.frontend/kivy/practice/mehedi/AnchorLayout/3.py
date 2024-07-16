from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout

class MyApp(App):
    def build(self):
        return AnchorLayout()

if __name__ == '__main__':
    MyApp().run()

