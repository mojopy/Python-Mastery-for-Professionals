from kivy.app import App
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.textinput import TextInput

class ScatterTextInputApp(App):
    def build(self):
        layout = ScatterLayout()

        # Movable and resizable text input field
        txt_input = TextInput(text="Move or resize me!", size_hint=(0.5, 0.2))
        layout.add_widget(txt_input)

        return layout

ScatterTextInputApp().run()
