from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button

class RelativeLayoutDynamicApp(App):
    def build(self):
        layout = RelativeLayout()

        # Button that takes up 50% of the width and height, centered
        layout.add_widget(Button(text="Big Center", size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.5}))

        # Small button in the top-right corner
        layout.add_widget(Button(text="Top Right", size_hint=(0.1, 0.1), pos_hint={'right': 1, 'top': 1}))

        # Button in the bottom-left corner, occupying 20% width and height
        layout.add_widget(Button(text="Bottom Left", size_hint=(0.2, 0.2), pos_hint={'x': 0, 'y': 0}))

        return layout

RelativeLayoutDynamicApp().run()
