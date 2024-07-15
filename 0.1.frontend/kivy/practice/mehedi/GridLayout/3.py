from kivy.app import App 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = GridLayout(cols=2)

        for i in range (1, 9):
            layout.add_widget(Label(text=f'Label {i}'))
            layout.add_widget(Button(text=f'Button {i}'))

        return layout
        
if __name__ == '__main__':
    MyApp().run()