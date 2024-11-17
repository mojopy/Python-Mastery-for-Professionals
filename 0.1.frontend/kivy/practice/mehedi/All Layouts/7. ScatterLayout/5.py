from kivy.app import App
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.button import Button

class RotatableButtonApp(App):
    def build(self):
        layout = ScatterLayout(do_rotation=True, do_scale=True)

        # Button that can be rotated and scaled
        btn = Button(text="Rotate & Scale Me", size_hint=(0.3, 0.2))
        layout.add_widget(btn)

        return layout

RotatableButtonApp().run()
