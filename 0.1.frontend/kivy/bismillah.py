from kivy.app import App
from kivy.uix.label import Label

class BismillahApp(App):
    def build(self):
        return Label(text="Bismillah")
    
if __name__ == "__main__":
    BismillahApp().run()