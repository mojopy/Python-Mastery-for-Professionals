from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class MyFloatLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text='Enter text:', size_hint=(.2, .1), pos_hint={'x': .1, 'top': 1}))
        self.text_input = TextInput(size_hint=(.6, .1), pos_hint={'x': .3, 'top': 1})
        self.add_widget(self.text_input)
        self.add_widget(Button(text='Submit', size_hint=(.2, .1), pos_hint={'x': .7, 'y': .8}, on_press=self.on_button_press))

    def on_button_press(self, instance):
        self.add_widget(Label(text=f'You entered: {self.text_input.text}', size_hint=(.5, .1), pos_hint={'center_x': .5, 'y': .6}))

class MyApp(App):
    def build(self):
        return MyFloatLayout()

if __name__ == '__main__':
    MyApp().run()