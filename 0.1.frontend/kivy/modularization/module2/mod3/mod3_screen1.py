from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class Mod3Screen1(Screen):
    def __init__(self, **kwargs):
        super(Mod3Screen1, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        label = Label(text='Module 3 - Screen 1')
        button = Button(text='Go to Screen 2', on_press=self.go_to_screen2)
        layout.add_widget(label)
        layout.add_widget(button)
        self.add_widget(layout)

    def go_to_screen2(self, instance):
        self.manager.current = 'mod3_screen2'
