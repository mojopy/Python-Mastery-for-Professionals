from kivy.app import App 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        outer_layout = GridLayout(cols=1)

        layout = GridLayout(cols=3)
        layout.add_widget(Label(text="Label 1"))
        layout.add_widget(Button(text="Button 1"))
        layout.add_widget(Label(text="Label 2"))
        layout.add_widget(Button(text="Button 2"))
        layout.add_widget(Label(text="Label 3"))
        layout.add_widget(Button(text="Button 3"))

        outer_layout.add_widget(Label(text="Outer Label 1"))
        outer_layout.add_widget(layout)
        outer_layout.add_widget(Label(text="outer Label 2"))

        return outer_layout

if __name__ =="__main__":
    MyApp().run()