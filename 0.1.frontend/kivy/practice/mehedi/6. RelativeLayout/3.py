from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button

class BottomLeftButtonApp(App):
    def build(self):
        layout = RelativeLayout()

        # Button positioned at the bottom left
        btn = Button(text="Bottom Left", size_hint=(0.2, 0.1), pos_hint={'x': 0, 'y': 0})
        layout.add_widget(btn)

        return layout

BottomLeftButtonApp().run()
