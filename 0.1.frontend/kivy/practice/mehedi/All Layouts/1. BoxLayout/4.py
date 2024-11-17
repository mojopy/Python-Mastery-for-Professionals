from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build (self):
        layout = BoxLayout(orientation='horizontal', spacing=10, padding=10)

        layout.add_widget(Button(text='1', size_hint=(1, .1)))
        layout.add_widget(Button(text='2', size_hint=(1, .2)))
        layout.add_widget(Button(text='3', size_hint=(.3, 1)))
        layout.add_widget(Button(text='4', size_hint=(.4, 1)))
        layout.add_widget(Button(text='5', size_hint=(.5, 1)))

        return layout
    
if __name__ == '__main__':
    MyApp().run()