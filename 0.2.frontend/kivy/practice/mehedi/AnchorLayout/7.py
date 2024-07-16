from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = AnchorLayout()

        top_left_button = Button(text='Top Left', size_hint=(None, None), size=(100, 50))
        top_left_button.pos_hint = {'x': 0, 'top': 1}
        layout.add_widget(top_left_button)

        top_right_button = Button(text='Top Right', size_hint=(None, None), size=(100, 50))
        top_right_button.pos_hint = {'right': 1, 'top': 1}
        layout.add_widget(top_right_button)

        bottom_left_button = Button(text='Bottom Left', size_hint=(None, None), size=(100, 50))
        bottom_left_button.pos_hint = {'x': 0, 'y': 0}
        layout.add_widget(bottom_left_button)

        bottom_right_button = Button(text='Bottom Right', size_hint=(None, None), size=(100, 50))
        bottom_right_button.pos_hint = {'right': 1, 'y': 0}
        layout.add_widget(bottom_right_button)

        return layout

if __name__ == '__main__':
    MyApp().run()
