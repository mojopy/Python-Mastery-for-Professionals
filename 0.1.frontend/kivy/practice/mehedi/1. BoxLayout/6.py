from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class MyApp (App):
    def build (self):
        outer_box = BoxLayout(orientation='vertical')

        inner_box = BoxLayout(orientation='horizontal')
        inner_box.add_widget(Button(text='Button 1'))
        inner_box.add_widget(Button(text='Button 2'))
        inner_box.add_widget(Button(text='Button 3'))

        outer_box.add_widget(Label(text='This is the top label'))
        outer_box.add_widget(inner_box)
        outer_box.add_widget(Label(text='This is the bottom label'))

        return outer_box
    
if __name__ == '__main__':
    MyApp().run()