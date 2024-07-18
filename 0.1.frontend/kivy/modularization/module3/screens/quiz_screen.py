from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class QuizScreen(Screen):
    def __init__(self, **kwargs):
        super(QuizScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        
        backButton = Button(text="Go back")
        backButton.bind(on_press=self.changeScreen)
        
        layout.add_widget(backButton)
        self.add_widget(layout)
    
    def changeScreen(self, instance):
        self.manager.current = 'main'