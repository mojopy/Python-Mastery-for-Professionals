from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button

class HorizontalStackLayoutExample(App):
    def build(self):
        layout = StackLayout(orientation='tb-rl', padding=10, spacing=10)

        for i in range(10):
            btn = Button(text=str(i+1), size_hint=(None, None), size=(100, 50))
            layout.add_widget(btn)
        
        return layout

if __name__ == '__main__':
    HorizontalStackLayoutExample().run()
