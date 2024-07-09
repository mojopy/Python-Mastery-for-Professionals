from kivy.app import App 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = GridLayout(cols=2)

        layout.add_widget(Label(text='Label 1'))
        layout.add_widget(Button(text='Button 1'))
        layout.add_widget(Label(text='Label 2'))
        layout.add_widget(Button(text='Button 2'))
        layout.add_widget(Label(text='Label 3'))
        layout.add_widget(Button(text='Button'))
        layout.add_widget(Label(text='Label 4'))
        layout.add_widget(Button(text='Button 4'))

        return layout
    
if __name__ == '__main__':
    MyApp().run()