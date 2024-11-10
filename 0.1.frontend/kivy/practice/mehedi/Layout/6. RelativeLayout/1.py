from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button

class SimpleRelativeLayoutApp(App):
    def build(self):
        layout = RelativeLayout()

        # Button at the top-left corner
        btn1 = Button(text="Top Left", size_hint=(0.2, 0.1), pos_hint={'x': 0, 'y': 0.9})
        layout.add_widget(btn1)

        # Button at the center
        btn2 = Button(text="Center", size_hint=(0.2, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(btn2)

        # Button at the bottom-right corner
        btn3 = Button(text="Bottom Right", size_hint=(0.2, 0.1), pos_hint={'x': 0.8, 'y': 0})
        layout.add_widget(btn3)

        return layout

SimpleRelativeLayoutApp().run()
