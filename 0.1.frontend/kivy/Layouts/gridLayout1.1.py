import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 3  # Number of columns in the grid layout

        # Add buttons to the grid layout
        self.add_widget(Button(text='Button 1'))
        self.add_widget(Button(text='Button 2'))
        self.add_widget(Button(text='Button 3'))
        self.add_widget(Button(text='Button 4'))

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MyApp().run()
