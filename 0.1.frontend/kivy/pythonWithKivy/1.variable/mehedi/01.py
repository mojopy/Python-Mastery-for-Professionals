from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        message = "Hello, Kivy!"

        label = Label(text=message, font_size=50)

        layout.add_widget(label)

        return layout

MyApp().run()