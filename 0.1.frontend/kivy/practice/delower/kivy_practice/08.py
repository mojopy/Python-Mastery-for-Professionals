from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.button import Button 
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        outer_box = BoxLayout(orientation = "vertical", spacing = 10, padding= 10)


        inner_box1 = BoxLayout(orientation="horizontal", spacing = 5, padding = 5)
        inner_box1.add_widget(Label(text="Inner Box 1 - Label 1"))
        inner_box1.add_widget(Button(text="Inner Box 1 -Button 1"))
        inner_box1.add_widget(Button(text="Inner Box 1 - Button 2"))


        inner_box2 = BoxLayout(orientation="horizontal",spacing = 5, padding = 5)
        inner_box2.add_widget(Label(text="Inner Box 2 - Label 1"))
        inner_box2.add_widget(Button(text="Inner Box 2 - Button 1"))
        inner_box2.add_widget(Button(text="Inner Box 2 - Button 2"))

        outer_box.add_widget(inner_box1)
        outer_box.add_widget(Label(text="Label between inner boxes"))
        outer_box.add_widget(inner_box2)

        return outer_box 

if __name__=="__main__":
    MyApp().run()