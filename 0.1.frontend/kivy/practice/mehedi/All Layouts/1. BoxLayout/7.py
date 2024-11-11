from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        outer_box = BoxLayout(orientation='vertical', spacing=10, padding=10)

        inner_box1 = BoxLayout(orientation='horizontal', spacing=5, padding=5)
        inner_box1.add_widget(Label(text='top label 1'))
        inner_box1.add_widget(Button(text='top button 1'))
        inner_box1.add_widget(Button(text='top btton 2'))

        inner_box2 = BoxLayout(orientation='horizontal', spacing=5, padding=5)
        inner_box2.add_widget(Label(text='down label 1'))
        inner_box2.add_widget(Button(text='down button 1'))
        inner_box2.add_widget(Button(text='down button 2'))

        outer_box.add_widget(inner_box1)
        outer_box.add_widget(Label(text='This is middle lebel'))
        outer_box.add_widget(inner_box2)

        return outer_box
    
if __name__ == '__main__':
    MyApp().run()