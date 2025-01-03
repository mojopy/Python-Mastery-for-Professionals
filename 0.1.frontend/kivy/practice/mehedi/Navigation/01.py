from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.add_widget(Button(text='Go to second screen', on_press=self.change_screen))

    def change_screen(self, *args):
        self.manager.current='second'

class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)
        self.add_widget(Button(text='Back to main screen', on_press=self.change_screen))

    def change_screen(self, *args):
        self.manager.current='main'

class MyScreenManagerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(SecondScreen(name='second'))

        return sm

if __name__ == '__main__':
    MyScreenManagerApp().run()