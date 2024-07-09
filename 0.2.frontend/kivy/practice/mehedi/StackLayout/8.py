from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button

class CustomPaddingSpacingStackLayoutExample(App):
    def build(self):
        layout = StackLayout(orientation='lr-tb', padding=[20, 40, 60, 80], spacing=[15, 25])

        for i in range(10):
            btn = Button(text=str(i+1), size_hint=(None, None), size=(100, 50))
            layout.add_widget(btn)
        
        return layout

if __name__ == '__main__':
    CustomPaddingSpacingStackLayoutExample().run()
