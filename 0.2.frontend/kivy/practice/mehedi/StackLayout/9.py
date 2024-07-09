from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button

class GridLikeStackLayoutExample(App):
    def build(self):
        layout = StackLayout(orientation='lr-tb', padding=10, spacing=10)

        for i in range(3):
            for j in range(3):
                btn = Button(text=f'{i+1},{j+1}', size_hint=(None, None), size=(100, 100))
                layout.add_widget(btn)
        
        return layout

if __name__ == '__main__':
    GridLikeStackLayoutExample().run()
