from kivy.app import App 
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button

class MyApp(App):
    def build (self):
        layout = AnchorLayout()

        button = Button(text='Button', size_hint=(None, None), size=(150,50))
        button.pos_hint = {'center_x': 0.6, 'center_y': 0.6}
        layout.add_widget(button)

        return layout
    
if __name__ == '__main__':
    MyApp().run()