from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.button import Button 
from kivy.uix.gridlayout import GridLayout

class MyApp(App):
    def build(self):
        layout = GridLayout(cols = 3)

        layout.add_widget(Label(text="Label 1"))
        layout.add_widget(Button(text="Button 1"))
        layout.add_widget(Label(text="Label 2"))
        layout.add_widget(Button(text="Button 2"))
        layout.add_widget(Label(text="Label 3"))
        layout.add_widget(Button(text="Button 3"))
        layout.add_widget(Button(text="Button spanning 3 column"))
        layout.add_widget(Button(text="Button spanning 4 columns"))
        layout.add_widget(Label(text="Label 4"))

        return layout
if __name__ =="__main__":
    MyApp().run()