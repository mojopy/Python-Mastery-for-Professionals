from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class MyApp(App):
    def build(self):
        layout = FloatLayout()

        btn1 = Button(
            text='Button 1',
            size_hint=(.2, .1),
            pos_hint={'x': .1, 'y': .8}
        )
        layout.add_widget(btn1)

        btn2 = Button(
            text='Button 2',
            size=(150, 50),
            size_hint=(None, None),
            pos=(200, 350)
        )
        layout.add_widget(btn2)

        label = Label(
            text='Center Label',
            size_hint=(.4, .2),
            pos_hint={'center_x': .5, 'center_y': .5}
        )
        layout.add_widget(label)

        return layout

if __name__ == '__main__':
    MyApp().run()
