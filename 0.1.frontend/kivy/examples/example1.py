import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import requests

class MyAPIApp(App):

    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Label to display API data
        self.label = Label(text="Press the button to See Today's Hadith")
        layout.add_widget(self.label)

        # Button to trigger API request
        button = Button(text="Today's Hadith")
        button.bind(on_press=self.fetch_data)
        layout.add_widget(button)

        return layout

    def fetch_data(self, instance):
        # Example API request to a placeholder API
        response = requests.get('http://127.0.0.1:8000/')

        if response.status_code == 200:
            data = response.json()
            # Update the label with fetched data
            self.label.text = data["message"]
        else:
            self.label.text = "Failed to fetch data"

if __name__ == '__main__':
    MyAPIApp().run()
