from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from data.questions import questions
from random import shuffle

class QuizScreen(Screen):
    def __init__(self, **kwargs):
        super(QuizScreen, self).__init__(**kwargs)
        self.current_question = 0
        self.score = 0
        
        self.layout = BoxLayout(orientation='vertical')
        self.question_label = Label(text=questions[self.current_question]['question'])
        
        self.buttons = [Button(text=option) for option in questions[self.current_question]['options']]
        for button in self.buttons:
            button.bind(on_press=self.check_answer)
        
        self.layout.add_widget(self.question_label)
        for button in self.buttons:
            self.layout.add_widget(button)
        
        self.add_widget(self.layout)
    
    def check_answer(self, instance):
        if instance.text == questions[self.current_question]['answer']:
            self.score += 1
        
        self.current_question += 1
        if self.current_question < len(questions):
            self.update_question()
        else:
            self.show_score()
    
    def update_question(self):
        question_data = questions[self.current_question]
        self.question_label.text = question_data['question']
        
        options = question_data['options']
        shuffle(options)
        for i, button in enumerate(self.buttons):
            button.text = options[i]
    
    def show_score(self):
        self.layout.clear_widgets()
        self.layout.add_widget(Label(text=f"Your score: {self.score}"))
        back_button = Button(text="Back to Main")
        back_button.bind(on_press=self.back_to_main)
        self.layout.add_widget(back_button)
    
    def back_to_main(self, instance):
        self.manager.current = 'main'
