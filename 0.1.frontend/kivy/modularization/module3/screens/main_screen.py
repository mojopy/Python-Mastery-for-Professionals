from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        
        start_quiz_button = Button(text="Start Quiz")
        start_quiz_button.bind(on_press=self.start_quiz)
        
        layout.add_widget(start_quiz_button)
        self.add_widget(layout)
    
    def start_quiz(self, instance):
        self.manager.current = 'quiz'