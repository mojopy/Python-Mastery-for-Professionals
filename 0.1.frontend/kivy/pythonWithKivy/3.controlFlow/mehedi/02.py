from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(text="Hello!")
    
    def change_text(self, instance):
        instance.text = "You clicked me!"

MyApp().run()