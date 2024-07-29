from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.button import Button 
from kivy.uix.floatlayout import FloatLayout

class FloatLayouApp(App):
    def build(self):
        layout = FloatLayout()

        self.label =Label(text="Hello, kivy!",size_hint=(.2, .1), pos_hint={"x":.4,"y":.8})

        layout.add_widget(self.label)

        button = Button(text="Click me",size_hint=(.2, .1),pos_hint={"x":.4,"y":.5})

        button.bind(on_press=self.on_button_click)

        layout.add_widget(button)

        return layout 
    
    def on_button_click(self, instance):
        self.label.text="Button Clicked!"

if __name__=="__main__":
    FloatLayouApp().run()

        
        