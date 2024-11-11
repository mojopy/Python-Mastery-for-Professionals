from kivy.app import App
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.button import Button

class TwoScatterButtonsApp(App):
    def build(self):
        layout = ScatterLayout()

        # First movable button
        btn1 = Button(text="Drag Me 1", size_hint=(0.3, 0.2))
        layout.add_widget(btn1)

        # Second movable button
        btn2 = Button(text="Drag Me 2", size_hint=(0.3, 0.2), pos=(200, 200))
        layout.add_widget(btn2)

        return layout

TwoScatterButtonsApp().run()
