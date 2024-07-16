from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class ScrollViewStackLayoutExample(App):
    def build(self):
        root = ScrollView(size_hint=(None, None), size=(400, 400))
        layout = StackLayout(orientation='lr-tb', padding=10, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        for i in range(30):
            btn = Button(text=f'Button {i+1}', size_hint=(None, None), size=(200, 50))
            layout.add_widget(btn)
        
        root.add_widget(layout)
        return root

if __name__ == '__main__':
    ScrollViewStackLayoutExample().run()
