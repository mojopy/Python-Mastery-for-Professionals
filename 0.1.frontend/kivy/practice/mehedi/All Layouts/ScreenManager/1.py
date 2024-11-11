from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

class FirstPage(Screen):
    def __init__(self, **kwargs):
        super(FirstPage, self).__init__(**kwargs)
        self.add_widget(Button(text='Go to 2nd page', on_press=self.change_screen))

    def change_screen(self, *args):
        self.manager.current = '2nd'

class SecondPage(Screen):
    def __init__(self, **kwargs):
        super(SecondPage, self).__init__(**kwargs)
        self.add_widget(Button(text='Go to 3rd page', on_press=self.change_screen))

    def change_screen(self, *args):
        self.manager.current = '3rd'

class ThirdPage(Screen):
    def __init__(self, **kwargs):
        super(ThirdPage, self).__init__(**kwargs)
        self.add_widget(Button(text='Go to main page', on_press=self.change_screen))

    def change_screen(self, *args):
        self.manager.current = 'main'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstPage(name='main'))
        sm.add_widget(SecondPage(name='2nd'))
        sm.add_widget(ThirdPage(name='3rd'))
        return sm
    
if __name__ == '__main__':
    MyApp().run()
