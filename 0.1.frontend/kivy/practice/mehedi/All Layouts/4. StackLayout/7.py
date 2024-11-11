from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button

class DynamicSizeHintStackLayoutExample(App):
    def build(self):
        layout = StackLayout(orientation='lr-tb', padding=10, spacing=10)

        for i in range(5):
            btn = Button(text=f'Button {i+1}', size_hint=(0.3, None), height=50)
            layout.add_widget(btn)
        
        return layout

if __name__ == '__main__':
    DynamicSizeHintStackLayoutExample().run()
