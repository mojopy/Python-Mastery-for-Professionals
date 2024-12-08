from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")

        number_label = Label(text="My favorite number is 95.")
        layout.add_widget(number_label)

        starting_label = Label(text="I like learning with Kivy.")
        layout.add_widget(starting_label)

        is_sunny = True
        weather_label = Label(text="Is it sunny? " + str(is_sunny))
        layout.add_widget(weather_label)

        button = Button(text="Change weather.")
        button.bind(on_press=self.change_weather)
        layout.add_widget(button)

        return layout
    
    def change_weather(self, instance):
        self.is_sunny = not self.is_sunny
        instance.parent.children[2].text = "Is it sunny? " + str(self.is_sunny)


if __name__ == "__main__":
    MyApp().run()