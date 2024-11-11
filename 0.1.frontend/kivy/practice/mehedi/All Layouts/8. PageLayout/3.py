from kivy.app import App 
from kivy.uix.pagelayout import PageLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MyApp(App):
    def build(self):
        layout = PageLayout()

        page1 = Label(text='Page 1: Label', font_size='30sp')
        page2 = Button(text='Page 2: button', font_size='20sp')
        page3 = TextInput(text='Page 3: TextInput', font_size='20sp')

        layout.add_widget(page1)
        layout.add_widget(page2)
        layout.add_widget(page3)

        return layout
    
if __name__ == '__main__':
    MyApp().run()