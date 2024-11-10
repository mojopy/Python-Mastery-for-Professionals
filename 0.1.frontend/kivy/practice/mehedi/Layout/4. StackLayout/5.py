from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class NestedStackLayoutExample(App):
    def build(self):
        outer_layout = StackLayout(orientation='lr-tb', padding=10, spacing=10)

        for i in range(2):
            inner_layout = StackLayout(orientation='tb-rl',
            padding=5, spacing=5, size_hint=(None, None), size=(150, 300))
            
            for j in range(5):
                btn = Button(text=f'Button {i+1}-{j+1}',
                size_hint=(None, None), size=(140, 50))
                inner_layout.add_widget(btn)
            
            outer_layout.add_widget(inner_layout)
        
        return outer_layout

if __name__ == '__main__':
    NestedStackLayoutExample().run()
