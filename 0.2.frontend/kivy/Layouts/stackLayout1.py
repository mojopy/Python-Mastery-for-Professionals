import kivy
from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button

class MyStackLayout(StackLayout):
    def __init__(self, **kwargs):
        super(MyStackLayout, self).__init__(**kwargs)
        
        # Add buttons to the stack layout
        for i in range(1, 6):
            btn = Button(text=f'Button {i}', size_hint=(None, None), size=(100, 50))
            self.add_widget(btn)

class MyApp(App):
    def build(self):
        return MyStackLayout()

if __name__ == '__main__':
    MyApp().run()
