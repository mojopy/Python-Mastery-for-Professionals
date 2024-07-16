from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.image import Image

class ImageStackLayoutExample(App):
    def build(self):
        layout = StackLayout(orientation='lr-tb', padding=10, spacing=10)

        for i in range(1, 6):
            img = Image(source=f'image{i}.png', size_hint=(None, None), size=(200, 200))
            layout.add_widget(img)
        
        return layout

if __name__ == '__main__':
    ImageStackLayoutExample().run()
