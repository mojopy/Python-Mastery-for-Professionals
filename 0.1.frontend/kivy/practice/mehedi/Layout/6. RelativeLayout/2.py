from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button

class CenteredButtonApp(App):
    def build(self):
        layout = RelativeLayout()

        # Button centered in the layout
        centered_btn = Button(text="Centered Button", size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(centered_btn)

        return layout

CenteredButtonApp().run()
