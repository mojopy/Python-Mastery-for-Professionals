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
        # Access the parent ScreenManager and switch to nested_manager
        self.parent.current = 'nested_manager'

class NestedScreenManager(Screen):  # Changed from ScreenManager to Screen
    def __init__(self, **kwargs):
        super(NestedScreenManager, self).__init__(**kwargs)
        # Create an internal ScreenManager
        self.sm = ScreenManager()
        self.sm.add_widget(NestedScreen1(name='nested_screen1'))
        self.sm.add_widget(NestedScreen2(name='nested_screen2'))
        self.add_widget(self.sm)

class NestedScreen1(Screen):
    def __init__(self, **kwargs):
        super(NestedScreen1, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        btn1 = Button(text="Back to Main")
        btn1.bind(on_release=self.go_back)
        btn2 = Button(text="Go to Nested Screen 2")
        btn2.bind(on_release=self.go_to_screen2)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        self.add_widget(layout)
    
    def go_back(self, instance):
        # Access the root ScreenManager through parent references
        self.parent.parent.parent.current = 'main_screen'
    
    def go_to_screen2(self, instance):
        self.parent.current = 'nested_screen2'

class NestedScreen2(Screen):
    def __init__(self, **kwargs):
        super(NestedScreen2, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        btn1 = Button(text="Back to Main")
        btn1.bind(on_release=self.go_back)
        btn2 = Button(text="Go to Nested Screen 1")
        btn2.bind(on_release=self.go_to_screen1)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        self.add_widget(layout)
    
    def go_back(self, instance):
        # Access the root ScreenManager through parent references
        self.parent.parent.parent.current = 'main_screen'
    
    def go_to_screen1(self, instance):
        self.parent.current = 'nested_screen1'

class MainScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(MainScreenManager, self).__init__(**kwargs)
        # Create and add the main screen
        self.add_widget(FirstScreen(name='main_screen'))
        
        # Create and add the nested manager screen
        self.add_widget(NestedScreenManager(name='nested_manager'))

class MyApp(App):
    def build(self):
        return MainScreenManager()

if __name__ == '__main__':
    MyApp().run()