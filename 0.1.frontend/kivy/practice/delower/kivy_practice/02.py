from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation="horizontal")

        layout.add_widget(Button(text="YES"))
        layout.add_widget(Button(text="NO"))
        layout.add_widget(Button(text="VERY GOOD"))

        return layout
    
if __name__=="__main__":
    MyApp().run()