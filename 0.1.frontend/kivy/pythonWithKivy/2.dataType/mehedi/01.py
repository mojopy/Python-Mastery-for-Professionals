from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")

        number_label = Label(text="My favorite number is 9.")
        layout.add_widget(number_label)

        text_label = Label(text="I love Kivy!")
        layout.add_widget(text_label)

        button = Button(text="Click Me!")
        button.bind(on_press=self.change_text)
        layout.add_widget(button)

        self.text_label = Label(text="The text will change!")
        layout.add_widget(self.text_label)

        return layout
    
    def change_text(self, instance):
        self.text_label.text = "You clicked the button!"

if __name__ == "__main__":
    MyApp().run()