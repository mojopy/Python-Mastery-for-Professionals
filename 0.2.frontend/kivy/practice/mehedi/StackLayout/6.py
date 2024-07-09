from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class MixedWidgetsStackLayoutExample(App):
    def build(self):
        layout = StackLayout(orientation='lr-tb', padding=10, spacing=10)

        for i in range(3):
            layout.add_widget(Button(text=f'Button {i+1}', size_hint=(None, None), size=(200, 50)))
            layout.add_widget(Label(text=f'Label {i+1}', size_hint=(None, None), size=(200, 50)))
            layout.add_widget(TextInput(text=f'TextInput {i+1}', size_hint=(None, None), size=(200, 50)))
        
        return layout

if __name__ == '__main__':
    MixedWidgetsStackLayoutExample().run()
