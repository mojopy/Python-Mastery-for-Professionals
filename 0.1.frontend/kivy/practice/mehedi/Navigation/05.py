from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import ListProperty

class HistoryScreen(Screen):
    def __init__(self, name, **kwargs):
        super(HistoryScreen, self).__init__(**kwargs)
        self.name = name
        
        layout = BoxLayout(orientation='vertical')
        
        # Header with back button
        header = BoxLayout(size_hint_y=0.1)
        back_btn = Button(
            text='Back',
            size_hint_x=0.2,
            on_release=self.go_back
        )
        title = Label(text=name)
        header.add_widget(back_btn)
        header.add_widget(title)
        
        # Content area with navigation buttons
        content = BoxLayout(orientation='vertical')
        screens = ['home', 'profile', 'settings', 'help']
        for screen in screens:
            if screen != name:
                btn = Button(
                    text=f'Go to {screen}',
                    on_release=lambda x, s=screen: self.navigate_to(s)
                )
                content.add_widget(btn)
        
        layout.add_widget(header)
        layout.add_widget(content)
        self.add_widget(layout)
    
    def navigate_to(self, screen_name):
        app = App.get_running_app()
        app.navigation_history.append(self.name)
        app.root.transition = SlideTransition(direction='left')
        app.root.current = screen_name
    
    def go_back(self, *args):
        app = App.get_running_app()
        if app.navigation_history:
            previous_screen = app.navigation_history.pop()
            app.root.transition = SlideTransition(direction='right')
            app.root.current = previous_screen

class HistoryApp(App):
    navigation_history = ListProperty([])
    
    def build(self):
        sm = ScreenManager()
        screens = ['home', 'profile', 'settings', 'help']
        for screen in screens:
            sm.add_widget(HistoryScreen(name=screen))
        return sm

if __name__ == '__main__':
    HistoryApp().run()