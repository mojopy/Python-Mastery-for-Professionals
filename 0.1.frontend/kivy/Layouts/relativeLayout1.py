import kivy
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = RelativeLayout()

        # Add buttons to the relative layout with specific positions
        btn1 = Button(text='Button 1', size_hint=(None, None), size=(100, 50), pos_hint={'x': 0.1, 'y': 0.8})
        btn2 = Button(text='Button 2', size_hint=(None, None), size=(100, 50), pos_hint={'x': 0.4, 'y': 0.6})
        btn3 = Button(text='Button 3', size_hint=(None, None), size=(100, 50), pos_hint={'x': 0.7, 'y': 0.4})

        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)

        return layout

if __name__ == '__main__':
    MyApp().run()
