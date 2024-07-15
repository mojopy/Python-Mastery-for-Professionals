from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        l1 = Label(text="Hi")
        l2 = Label(text="Hello")
        b1 = Button(text="On")
        b2 = Button(text="Off")

        layout.add_widget(l1)
        layout.add_widget(l2)
        layout.add_widget(b1)
        layout.add_widget(b2)

        return layout
    
if __name__ == "__main__":
    MApp().run()