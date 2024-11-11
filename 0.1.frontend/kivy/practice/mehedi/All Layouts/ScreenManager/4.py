from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# Define two screens by inheriting from the Screen class
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        layout = BoxLayout()
        button = Button(text="Go to Settings")
        button.bind(on_press=self.switch_to_settings)
        layout.add_widget(button)
        self.add_widget(layout)

    def switch_to_settings(self, instance):
        self.manager.current = 'settings'

class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        layout = BoxLayout()
        button = Button(text="Go to Home")
        button.bind(on_press=self.switch_to_home)
        layout.add_widget(button)
        self.add_widget(layout)

    def switch_to_home(self, instance):
        self.manager.current = 'home'

# Main App Class
class MyApp(App):
    def build(self):
        # ScreenManager to handle screen transitions
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(SettingsScreen(name='settings'))
        return sm

if __name__ == "__main__":
    MyApp().run()