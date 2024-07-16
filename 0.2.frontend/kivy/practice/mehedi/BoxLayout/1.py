from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class FirstApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        b1 = Button(text="On")
        b2 = Button(text="Off")

        layout.add_widget(b1)
        layout.add_widget(b2)

        return layout
    
if __name__ == '__main__':
    FirstApp().run()