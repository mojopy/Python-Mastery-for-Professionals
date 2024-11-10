from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button

class RelativeLayoutExample(App):
    def build(self):
        layout = RelativeLayout()

        # Top-left positioned button
        layout.add_widget(Button(text="Top Left", size_hint=(0.2, 0.1), pos_hint={'x': 0, 'top': 1}))

        # Bottom-right positioned button
        layout.add_widget(Button(text="Bottom Right", size_hint=(0.2, 0.1), pos_hint={'right': 1, 'y': 0}))

        # Button positioned at the center
        layout.add_widget(Button(text="Center", size_hint=(0.2, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.5}))

        # Button positioned slightly towards the top-center
        layout.add_widget(Button(text="Top Center", size_hint=(0.2, 0.1), pos_hint={'center_x': 0.5, 'top': 1}))

        return layout

RelativeLayoutExample().run()
