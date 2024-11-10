from kivy.app import App
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.image import Image

class ScatterImageApp(App):
    def build(self):
        layout = ScatterLayout()

        # Add an image that can be moved and scaled
        img = Image(source='your_image_path.png', size_hint=(0.5, 0.5))
        layout.add_widget(img)

        return layout

ScatterImageApp().run()
