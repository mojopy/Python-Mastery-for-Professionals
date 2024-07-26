from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        main_layout = BoxLayout(orientation="vertical")

        inner_boxlayout = BoxLayout(orientation="horizontal")
        inner_boxlayout.add_widget(Button(text="Button 1"))
        inner_boxlayout.add_widget(Button(text="Button 2"))
        inner_boxlayout.add_widget(Button(text="Button 3"))

        main_layout.add_widget(Label(text="Label above inner box"))
        main_layout.add_widget(inner_boxlayout)
        main_layout.add_widget(Label(text="Label below inner box"))

        return main_layout

if __name__ =="__main__":
    MyApp().run()