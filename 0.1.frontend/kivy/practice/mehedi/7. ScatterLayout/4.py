from kivy.app import App
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image

class MultiWidgetScatterApp(App):
    def build(self):
        layout = ScatterLayout()

        # Movable button
        btn = Button(text="Move Button", size_hint=(0.2, 0.2))
        layout.add_widget(btn)

        # Movable label
        label = Label(text="Move Label", size_hint=(0.3, 0.1))
        layout.add_widget(label)

        # Movable image
        img = Image(source='your_image_path.png', size_hint=(0.4, 0.4))
        layout.add_widget(img)

        return layout

MultiWidgetScatterApp().run()
