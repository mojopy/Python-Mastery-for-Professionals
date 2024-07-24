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
        self.manager.current = 'nested_manager_screen'

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

class NestedScreenManager(Screen):
    def __init__(self, **kwargs):
        super(NestedScreenManager, self).__init__(**kwargs)
        nested_manager = ScreenManager()
        
        nested_screen1 = NestedScreen1(name='nested_screen1')
        nested_screen2 = NestedScreen2(name='nested_screen2')
        
        nested_manager.add_widget(nested_screen1)
        nested_manager.add_widget(nested_screen2)
        
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(nested_manager)
        self.add_widget(layout)
        
        # Set the default screen for the nested manager
        nested_manager.current = 'nested_screen1'

class MainScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(MainScreenManager, self).__init__(**kwargs)
        
        # Create and add the main screen
        first_screen = FirstScreen(name='main_screen')
        self.add_widget(first_screen)
        
        # Create the nested ScreenManager
        nested_screen_manager = NestedScreenManager(name='nested_manager_screen')
        self.add_widget(nested_screen_manager)

class MyApp(App):
    def build(self):
        return MainScreenManager()

if __name__ == '__main__':
    MyApp().run()
