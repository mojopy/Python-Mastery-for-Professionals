from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle

class ColoredPage(Widget):
    def __init__(self, color, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(*color)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

class MyApp(App):
    def build(self):
        layout = PageLayout()

        # Page 1 with red background
        page1 = ColoredPage(color=(1, 0, 0, 1))
        page1.add_widget(Label(text='Page 1: Red', font_size='30sp', color=(1, 1, 1, 1)))
        layout.add_widget(page1)

        # Page 2 with green background
        page2 = ColoredPage(color=(0, 1, 0, 1))
        page2.add_widget(Label(text='Page 2: Green', font_size='30sp', color=(1, 1, 1, 1)))
        layout.add_widget(page2)

        # Page 3 with blue background
        page3 = ColoredPage(color=(0, 0, 1, 1))
        page3.add_widget(Label(text='Page 3: Blue', font_size='30sp', color=(1, 1, 1, 1)))
        layout.add_widget(page3)

        return layout

if __name__ == '__main__':
    MyApp().run()
