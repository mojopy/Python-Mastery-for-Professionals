from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        anchor_layout = AnchorLayout()

        box_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(200, 150))
        box_layout.add_widget(Button(text='Button 1'))
        box_layout.add_widget(Button(text='Button 2'))
        box_layout.add_widget(Button(text='Button 3'))

        box_layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        anchor_layout.add_widget(box_layout)

        return anchor_layout

if __name__ == '__main__':
    MyApp().run()
