from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super(FirstScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        btn = Button(text="Go to Nested Manager")
        btn.bind(on_release=self.go_to_nested)
        layout.add_widget(btn)
        self.add_widget(layout)
    
    def go_to_nested(self, instance):
        self.manager.current = 'nested_manager'

class NestedScreenManager(ScreenManager):
    pass

class NestedScreen1(Screen):
    def __init__(self, **kwargs):
        super(NestedScreen1, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        btn = Button(text="Back to Main")
        btn.bind(on_release=self.go_back)
        layout.add_widget(btn)
        self.add_widget(layout)
    
    def go_back(self, instance):
        self.manager.current = 'main_screen'

class NestedScreen2(Screen):
    def __init__(self, **kwargs):
        super(NestedScreen2, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        btn = Button(text="Back to Main")
        btn.bind(on_release=self.go_back)
        layout.add_widget(btn)
        self.add_widget(layout)
    
    def go_back(self, instance):
        self.manager.current = 'main_screen'

class MainScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(MainScreenManager, self).__init__(**kwargs)
        
        # Create and add the main screen
        first_screen = FirstScreen()
        first_screen.name = 'main_screen'
        self.add_widget(first_screen)
        
        # Create the nested ScreenManager
        nested_manager = NestedScreenManager()
        nested_manager.name = 'nested_manager'
        nested_manager.add_widget(NestedScreen1(name='nested_screen1'))
        nested_manager.add_widget(NestedScreen2(name='nested_screen2'))
        
        # Add the nested manager to the main screen manager
        self.add_widget(nested_manager)

class MyApp(App):
    def build(self):
        return MainScreenManager()

if __name__ == '__main__':
    MyApp().run()
