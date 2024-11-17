from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        layout = FloatLayout()

        btn1 = Button(
            text='Button 1',
            size=(150, 50),
            size_hint=(None, None),
            pos=(100, 400)
        )
        layout.add_widget(btn1)

        btn2 = Button(
            text='Button 2',
            size=(200, 50),
            size_hint=(None, None),
            pos=(300, 200)
        )
        layout.add_widget(btn2)

        return layout

if __name__ == '__main__':
    MyApp().run()
