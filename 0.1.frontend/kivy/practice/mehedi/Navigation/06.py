from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, FadeTransition
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class BaseScreen(Screen):
    def __init__(self, name, next_screen, **kwargs):
        super(BaseScreen, self).__init__(**kwargs)
        self.name = name
        self.next_screen = next_screen
        
        layout = BoxLayout(orientation='vertical')
        label = Label(text=f'Screen {name}')
        
        buttons_layout = BoxLayout(size_hint_y=0.2)
        prev_btn = Button(text='Previous')
        next_btn = Button(text='Next')
        
        prev_btn.bind(on_release=self.go_previous)
        next_btn.bind(on_release=self.go_next)
        
        buttons_layout.add_widget(prev_btn)
        buttons_layout.add_widget(next_btn)
        
        layout.add_widget(label)
        layout.add_widget(buttons_layout)
        self.add_widget(layout)
    
    def go_previous(self, *args):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = f'screen{int(self.name[-1])-1}'
    
    def go_next(self, *args):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = f'screen{self.next_screen}'

class TransitionApp(App):
    def build(self):
        sm = ScreenManager()
        
        # Add 4 screens
        screens = [
            BaseScreen('screen1', 2),
            BaseScreen('screen2', 3),
            BaseScreen('screen3', 4),
            BaseScreen('screen4', 1)
        ]
        
        for screen in screens:
            sm.add_widget(screen)
            
        return sm

if __name__ == '__main__':
    TransitionApp().run()