from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class FirstApp(App):
    def build(self):
        layout = BoxLayout(orientation='horizontal')

        a = Button(text="Hi")
        b = Button(text="Hello")
        c = Button(text="ok")

        layout.add_widget(a)
        layout.add_widget(b)
        layout.add_widget(c)

        return layout
    
if __name__ == '__main__':
    FirstApp().run()