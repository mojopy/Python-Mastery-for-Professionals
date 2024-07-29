from kivy.app import App 
from kivy.uix.button import Button 
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", spacing = 10, padding = 10)

        layout.add_widget(Button(text="Button 1", size_hint=(1, 0.2)))
        layout.add_widget(Button(text="Button 2", size_hint=(1, 0.5)))
        layout.add_widget(Button(text="Button 3", size_hint=(1, 1)))

        return layout
if __name__=="__main__":
    MyApp().run()