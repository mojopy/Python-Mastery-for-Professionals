from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        bg_color = [0, 1, 0, 1]

        Window.clearcolor = bg_color

        label = Label(text="Green is Awesome!", font_size=50)

        layout.add_widget(label)

        return layout
    
MyApp().run()