from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        greet = "Hi, there!"
        return Label(text=greet)
    
if __name__ == '__main__':
        MyApp().run()