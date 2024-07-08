import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = FloatLayout()

        # Add buttons to the float layout with specific positions
        btn1 = Button(text='Button 1', size_hint=(None, None), size=(100, 50), pos=(100, 200))
        btn2 = Button(text='Button 2', size_hint=(None, None), size=(100, 50), pos=(300, 300))
        btn3 = Button(text='Button 3', size_hint=(None, None), size=(100, 50), pos=(500, 100))

        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)

        return layout

if __name__ == '__main__':
    MyApp().run()
