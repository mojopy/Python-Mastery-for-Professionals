from kivy.app import App
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.button import Button

class MovableOnlyButtonApp(App):
    def build(self):
        layout = ScatterLayout(do_rotation=False, do_scale=False)

        # Button that can only be moved, not rotated or scaled
        btn = Button(text="Move Only", size_hint=(0.3, 0.2))
        layout.add_widget(btn)

        return layout

MovableOnlyButtonApp().run()
