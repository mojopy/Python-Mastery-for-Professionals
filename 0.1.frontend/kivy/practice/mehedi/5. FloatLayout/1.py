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
            pos_hint={'x': .5, 'y': .8}
        )
        layout.add_widget(btn1)

        btn2 = Button(
            text='Button 2',
            size_hint=(.3, .1),
            pos_hint={'x': .5, 'y': .2}
        )
        layout.add_widget(btn2)

        label = Label(
            text='Hello, Kivy!',
            size_hint=(.4, .2),
            pos_hint={'x': .5, 'y': .5}
        )
        layout.add_widget(label)

        return layout
    
if __name__ == '__main__':
    MyApp().run()