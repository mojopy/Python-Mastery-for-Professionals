from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import ListProperty
from kivy.metrics import dp

class BreadcrumbBar(BoxLayout):
    def __init__(self, **kwargs):
        super(BreadcrumbBar, self).__init__(**kwargs)
        self.size_hint_y = None
        self.height = dp(40)
        self.update_breadcrumbs([])
    
    def update_breadcrumbs(self, path):
        self.clear_widgets()
        for i, screen in enumerate(path):
            if i > 0:
                self.add_widget(Label(
                    text='>', 
                    size_hint_x=None, 
                    width=dp(20)
                ))
            btn = Button(
                text=screen,
                size_hint_x=None,
                width=dp(100),
                on_release=lambda x, s=screen: self.navigate_to(s)
            )
            self.add_widget(btn)
    
    def navigate_to(self, screen_name):
        app = App.get_running_app()
        current_path = app.screen_path
        if screen_name in current_path:
            index = current_path.index(screen_name)
            app.screen_path = current_path[:index + 1]
            app.root.ids.sm.current = screen_name

class BreadcrumbScreen(Screen):
    def __init__(self, name, **kwargs):
        super(BreadcrumbScreen, self).__init__(**kwargs)
        self.name = name
        
        layout = BoxLayout(orientation='vertical')
        content = BoxLayout(orientation='vertical')
        
        # Add navigation buttons
        screens = {
            'home': ['profile', 'settings'],
            'profile': ['details', 'preferences'],
            'settings': ['account', 'privacy'],
            'details': ['personal', 'professional'],
            'preferences': ['theme', 'notifications']
        }
        
        if name in screens:
            for screen in screens[name]:
                btn = Button(
                    text=f'Go to {screen}',
                    on_release=lambda x, s=screen: self.navigate_to(s)
                )
                content.add_widget(btn)
        
        layout.add_widget(content)
        self.add_widget(layout)
    
    def navigate_to(self, screen_name):
        app = App.get_running_app()
        app.screen_path.append(screen_name)
        app.root.ids.breadcrumb.update_breadcrumbs(app.screen_path)
        app.root.ids.sm.current = screen_name

class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'

class BreadcrumbApp(App):
    screen_path = ListProperty(['home'])
    
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    BreadcrumbApp().run()