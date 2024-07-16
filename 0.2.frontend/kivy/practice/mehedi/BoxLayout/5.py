from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        b1 = Button(text='Button 1', size_hint=(1, 0.2))
        b2 = Button(text='Button 2', size_hint=(1, 0.5))
        b3 = Button(text='Button 3', size_hint=(1, 1))

        layout.add_widget(b1)
        layout.add_widget(b2)
        layout.add_widget(b3)

        return layout

if __name__ == '__main__':
    MyApp().run()
