from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")

        layout.add_widget(Label(text="Hi"))
        layout.add_widget(Label(text="Hello"))
        layout.add_widget(Button(text="On"))
        layout.add_widget(Button(text="Off"))

        return layout
if __name__ == "__main__":
    MyApp().run()