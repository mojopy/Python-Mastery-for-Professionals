from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = AnchorLayout()

        top_button = Button(text='Top Center', size_hint=(None, None), size=(150, 50))
        top_button.pos_hint = {'center_x': 0.5, 'top': 1}
        layout.add_widget(top_button)

        bottom_button = Button(text='Bottom Center', size_hint=(None, None), size=(150, 50))
        bottom_button.pos_hint = {'center_x': 0.5, 'y': 0}
        layout.add_widget(bottom_button)

        return layout

if __name__ == '__main__':
    MyApp().run()
