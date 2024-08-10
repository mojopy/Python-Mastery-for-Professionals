from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class MyApp(App):
    def build(self):
        layout = FloatLayout()

        layout.add_widget(Button(text="Button 1", size_hint=(.2, .2), pos_hint={"x":.1, "y":.3}))
        layout.add_widget(Button(text="Button 2", size_hint=(.2, .4), pos_hint={"x":.5, "y":.3}))

        return layout
if __name__=="__main__":
    MyApp().run()
