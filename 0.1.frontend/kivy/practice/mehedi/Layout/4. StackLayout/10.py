from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class ToolbarExample(App):
    def build(self):
        layout = StackLayout(orientation='lr-tb',
                padding=10, spacing=10, size_hint_y=None, height=60)

        layout.add_widget(Button(text='Home', size_hint=(None, None),
                        size=(100, 50)))
        layout.add_widget(Button(text='Settings', size_hint=(None, None),
                        size=(100, 50)))
        layout.add_widget(Button(text='Help', size_hint=(None, None),
                        size=(100, 50)))
        layout.add_widget(Button(text='About', size_hint=(None, None),
                        size=(100, 50)))
        
        return layout

if __name__ == '__main__':
    ToolbarExample().run()
