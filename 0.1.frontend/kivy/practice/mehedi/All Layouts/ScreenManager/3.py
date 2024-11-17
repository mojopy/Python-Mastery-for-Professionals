from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, FadeTransition, SwapTransition


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.add_widget(Button(text='Go to Second Screen', on_press=self.change_screen))

    def change_screen(self, *args):
        self.manager.current = 'second'

    def on_enter(self):
        print("Entered MainScreen")

    def on_leave(self):
        print("Left MainScreen")

class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)
        self.add_widget(Button(text='Back to Main Screen', on_press=self.change_screen))

    def change_screen(self, *args):
        self.manager.current = 'main'

    def on_enter(self):
        print("Entered SecondScreen")

    def on_leave(self):
        print("Left SecondScreen")

class MyScreenManagerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(SecondScreen(name='second'))
        return sm
    
if __name__ == '__main__':
    MyScreenManagerApp().run()