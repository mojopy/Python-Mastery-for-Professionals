from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(text="Click Me!")
    
    def on_press(self, instance):
        instance.text = "You clicked me!"

if __name__ == "__main__":
    MyApp().run()