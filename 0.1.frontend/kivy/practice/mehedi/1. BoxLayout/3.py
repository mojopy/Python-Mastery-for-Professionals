from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build (self):
        main_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        top_layout = BoxLayout(orientation='horizontal', spacing=5)
        top_layout.add_widget(Button(text='Top Left Button'))
        top_layout.add_widget(Button(text='Top Right Button'))

        middle_layout = BoxLayout(orientation='horizontal', spacing=5)
        middle_layout.add_widget(Button(text='Middle Left Button'))
        middle_layout.add_widget(Button(text='Middle Right Button'))

        bottom_layout = BoxLayout(orientation='horizontal', spacing=5)
        bottom_layout.add_widget(Button(text='Bottom Left Button'))
        bottom_layout.add_widget(Button(text='Bottom Right Layout'))

        main_layout.add_widget(top_layout)
        main_layout.add_widget(middle_layout)
        main_layout.add_widget(bottom_layout)

        return main_layout
    
if __name__ == '__main__':
    MyApp().run()