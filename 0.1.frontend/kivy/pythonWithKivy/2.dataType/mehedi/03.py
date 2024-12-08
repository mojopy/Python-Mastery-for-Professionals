from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        number = 3
        text = "I love Kivy!"

        return Button(text=f"Number: {number}, Text: {text}")
    
if __name__ == "__main__":
    MyApp().run()