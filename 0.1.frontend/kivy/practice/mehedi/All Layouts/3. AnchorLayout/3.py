from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button

class MyApp (App):
    def build(self):
        layout = AnchorLayout()
        top_right_button = Button(text='Top Right', size_hint=(None, None), size=(100, 50))
        top_right_button.pos_hint = {'right': 1, 'top': 1}
        layout.add_widget(top_right_button)

        return layout
    
if __name__ == '__main__':
    MyApp().run()