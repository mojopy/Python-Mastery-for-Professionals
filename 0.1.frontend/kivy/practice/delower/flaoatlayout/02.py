from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

class MyApp(App):
    def build(self):
        layout = FloatLayout()

        layout.add_widget(Label(text="Hello", size_hint=(0.3, 0.3), pos_hint={"center_x": 0.2, "center_y": 0.5}))
        layout.add_widget(Label(text="there", size_hint=(0.5, 0.6), pos_hint={"center_x": 0.5, "center_y": 0.1}))

        return layout

if __name__ =="__main__":
    MyApp().run()