from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        layout = AnchorLayout(padding=[50, 50, 50, 50])
        label = Label(text='Centered Label', size_hint=(None, None), size=(200, 50))
        #label.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        layout.add_widget(label)
        return layout

if __name__ == '__main__':
    MyApp().run()
