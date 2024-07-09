from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle

class ColoredBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(0.2, 0.6, 0.8, 1)  # Set the background color (r, g, b, a)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        
        self.bind(size=self._update_rect, pos=self._update_rect)
    
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class MyBoxLayoutApp(App):
    def build(self):
        # Create a ColoredBoxLayout with vertical orientation
        layout = ColoredBoxLayout(orientation='vertical', spacing=10, padding=[20, 10, 20, 10])
        
        # Create buttons with different size hints
        button1 = Button(text='Button 1', size_hint=(1, 0.2))
        button2 = Button(text='Button 2', size_hint=(1, 0.3))
        button3 = Button(text='Button 3', size_hint=(1, 0.5))
        
        # Add buttons to the layout
        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)
        
        return layout

if __name__ == '__main__':
    MyBoxLayoutApp().run()
