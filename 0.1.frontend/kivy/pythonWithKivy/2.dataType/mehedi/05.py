from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")

        number_label = Label(text="My number is 5.")
        layout.add_widget(number_label)

        starting_label = Label(text="I like Kive.")
        layout.add_widget(starting_label)

        bool_label = Label(text="Click me!")
        layout.add_widget(bool_label)

        button = Button(text="Click me!")
        button.bind(on_press=self.change_text)
        layout.add_widget(button)

        return layout
    
    def change_text(self, instance):
        instance.text = "You clicked me!"

if __name__ == "__main__":
    MyApp().run()