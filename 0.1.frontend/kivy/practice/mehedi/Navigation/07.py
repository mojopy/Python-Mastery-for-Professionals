from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.metrics import dp
from kivy.core.window import Window

class DrawerScreen(Screen):
    def __init__(self, name, **kwargs):
        super(DrawerScreen, self).__init__(**kwargs)
        self.name = name
        
        layout = BoxLayout(orientation='vertical', padding=dp(10))
        content = Label(text=f'{name} Content')
        layout.add_widget(content)
        
        self.add_widget(layout)

class DrawerMenu(BoxLayout):
    def __init__(self, screen_manager, **kwargs):
        super(DrawerMenu, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint_x = None
        self.width = dp(200)
        self.sm = screen_manager
        self.is_open = False
        
        # Create menu items
        menu_items = ['Home', 'Profile', 'Settings', 'Help']
        for item in menu_items:
            btn = Button(
                text=item,
                size_hint_y=None,
                height=dp(50),
                on_release=lambda x, i=item: self.select_item(i.lower())
            )
            self.add_widget(btn)
    
    def select_item(self, item_name):
        self.sm.current = item_name
        self.toggle_drawer()
    
    def toggle_drawer(self):
        target_x = 0 if not self.is_open else -self.width
        anim = Animation(x=target_x, duration=0.3)
        anim.start(self)
        self.is_open = not self.is_open

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        
        # Create screen manager
        self.sm = ScreenManager()
        screens = ['home', 'profile', 'settings', 'help']
        for screen in screens:
            self.sm.add_widget(DrawerScreen(name=screen))
        
        # Create drawer menu
        self.drawer = DrawerMenu(self.sm)
        self.drawer.x = -self.drawer.width
        
        # Create menu button
        menu_button = Button(
            text='Menu',
            size_hint=(None, None),
            size=(dp(50), dp(50)),
            pos_hint={'top': 1}
        )
        menu_button.bind(on_release=lambda x: self.drawer.toggle_drawer())
        
        # Add widgets
        self.add_widget(self.sm)
        self.add_widget(menu_button)
        self.add_widget(self.drawer)

class DrawerApp(App):
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    DrawerApp().run()