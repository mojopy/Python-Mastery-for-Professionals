from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(text="Click me!")
    
    def say_hello(self, instance):
        print("Hello, you clicked the button.")

MyApp().run()