from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class FormLayoutExample(App):
    def build(self):
        layout = StackLayout(orientation='lr-tb', padding=10, spacing=10)

        layout.add_widget(Label(text='Name:', size_hint=(None, None), size=(100, 50)))
        layout.add_widget(TextInput(size_hint=(None, None), size=(200, 50)))
        
        layout.add_widget(Label(text='Email:', size_hint=(None, None), size=(100, 50)))
        layout.add_widget(TextInput(size_hint=(None, None), size=(200, 50)))

        layout.add_widget(Label(text='Phone:', size_hint=(None, None), size=(100, 50)))
        layout.add_widget(TextInput(size_hint=(None, None), size=(200, 50)))
        
        layout.add_widget(Button(text='Submit', size_hint=(None, None), size=(300, 50)))
        
        return layout

if __name__ == '__main__':
    FormLayoutExample().run()
