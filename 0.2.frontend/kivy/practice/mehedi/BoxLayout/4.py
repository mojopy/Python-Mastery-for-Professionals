from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='horizontal', spacing=10, padding=10)

        btn1 = Button(text='Button 1', size_hint=(0.2, 1))
        btn2 = Button(text='Button 2', size_hint=(0.5, 1))
        btn3 = Button(text='Button 3', size_hint=(1, 1))

        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)

        return layout

if __name__ == '__main__':
    MyApp().run()
