from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class Mod3Screen2(Screen):
    def __init__(self, **kwargs):
        super(Mod3Screen2, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        label = Label(text='Module 3 - Screen 2')
        button = Button(text='Go to Screen 1', on_press=self.go_to_screen1)
        layout.add_widget(label)
        layout.add_widget(button)
        self.add_widget(layout)

    def go_to_screen1(self, instance):
        self.manager.current = 'mod3_screen1'
