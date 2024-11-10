from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class HomeScreen(Screen):
    def open_popup(self):
        layout = BoxLayout(orientation='vertical')
        popup_label = Label(text="This is a pop-up message!")
        close_button = Button(text="Close", size_hint=(1, 0.3))
        layout.add_widget(popup_label)
        layout.add_widget(close_button)
        popup = Popup(title="Popup", content=layout, size_hint=(0.6, 0.4))
        close_button.bind(on_press=popup.dismiss)
        popup.open()

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        return sm

if __name__ == '__main__':
    MyApp().run()
