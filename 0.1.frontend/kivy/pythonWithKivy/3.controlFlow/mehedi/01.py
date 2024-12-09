from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        self.button = Button(text="Click me!")
        self.button.bind(on_press=self.change_text)
        return self.button
    
    def change_text(self, instance):
        if self.button.text == "Click me!":
            self.button.text = "You clicked me."

        else:
            self.button.text = "Click me."

MyApp().run()