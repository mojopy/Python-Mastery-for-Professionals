from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = AnchorLayout(anchor_x='right', anchor_y='bottom')
        button = Button(text='Click Me', size_hint=(None, None), size=(100, 50))
        layout.add_widget(button)
        return layout

if __name__ == '__main__':
    MyApp().run()
