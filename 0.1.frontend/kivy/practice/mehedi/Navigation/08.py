from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.metrics import dp
from kivy.core.window import Window

class TabScreen(Screen):
    def __init__(self, name, **kwargs):
        super(TabScreen, self).__init__(**kwargs)
        self.name = name
        layout = BoxLayout(orientation='vertical')
        
        # Content area
        content = Label(
            text=f'{name} Content',
            size_hint_y=0.9
        )
        layout.add_widget(content)
        
        self.add_widget(layout)

class TabBar(BoxLayout):
    def __init__(self, screen_manager, **kwargs):
        super(TabBar, self).__init__(**kwargs)
        self.size_hint_y = None
        self.height = dp(50)
        self.sm = screen_manager
        
        # Create tab buttons
        tabs = ['Home', 'Profile', 'Messages', 'Settings']
        for tab in tabs:
            btn = Button(
                text=tab,
                on_release=lambda x, t=tab: self.switch_tab(t.lower())
            )
            self.add_widget(btn)
    
    def switch_tab(self, tab_name):
        self.sm.current = tab_name

class MainApp(App):
    def build(self):
        # Main layout
        layout = BoxLayout(orientation='vertical')
        
        # Screen manager for tabs
        sm = ScreenManager()
        
        # Add screens
        screens = ['home', 'profile', 'messages', 'settings']
        for screen in screens:
            sm.add_widget(TabScreen(name=screen))
        
        # Create layout with screen manager and tab bar
        layout.add_widget(sm)
        layout.add_widget(TabBar(sm))
        
        return layout

if __name__ == '__main__':
    MainApp().run()