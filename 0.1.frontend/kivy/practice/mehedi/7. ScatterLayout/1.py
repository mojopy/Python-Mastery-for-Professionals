from kivy.app import App
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.button import Button

class SimpleScatterApp(App):
    def build(self):
        layout = ScatterLayout()

        # A single movable button
        btn = Button(text="Drag Me", size_hint=(0.3, 0.2))
        layout.add_widget(btn)

        return layout

SimpleScatterApp().run()
