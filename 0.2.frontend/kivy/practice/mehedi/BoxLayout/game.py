import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

import random

class RandomNumberApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)


        self.layout = BoxLayout(orientation='vertical')

        self.numberLayout = BoxLayout(orientation='horizontal')
        self.result_label = Label(text='', size_hint_x=0.7, font_size='40sp', color=(0, 0, 0, 1))
        self.numberLayout.add_widget(self.result_label)

        self.setingsLayout = BoxLayout(orientation='vertical', size_hint_x=0.3)
        self.min_input = TextInput(hint_text='Enter minimum value', input_filter='int', multiline=False)
        self.max_input = TextInput(hint_text='Enter maximum value', input_filter='int', multiline=False)
        self.setingsLayout.add_widget(self.min_input)
        self.setingsLayout.add_widget(self.max_input)
        self.numberLayout.add_widget(self.setingsLayout)

        self.layout.add_widget(self.numberLayout)
        
        
        self.generate_button = Button(text='Generate Random Number')
        self.generate_button.bind(on_press=self.generate_random_number)
        self.layout.add_widget(self.generate_button)
        
        
        
        
        
        
        return self.layout
    
    def generate_random_number(self, instance):
        try:
            min_val = int(self.min_input.text)
            max_val = int(self.max_input.text)
            if min_val > max_val:
                self.result_label.text = "Min value should be less than Max value"
            else:
                random_number = random.randint(min_val, max_val)
                self.result_label.text = f'{random_number}'
        except ValueError:
            self.result_label.text = "Please enter valid integers"

if __name__ == '__main__':
    RandomNumberApp().run()
