from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button

class MyApp (App):
    def build (self):
        layout = AnchorLayout()
        center_button = Button(text='Center')
        layout.add_widget(center_button)

        return layout
    
if __name__ =='__main__':
    MyApp().run()