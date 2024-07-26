from kivy.app import App
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle

class ColoredAccordionItem(AccordionItem):
    def __init__(self, **kwargs):
        color = kwargs.pop('color', (1, 1, 1, 1))
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(*color)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class MyApp(App):
    def build(self):
        accordion = Accordion()

        item1 = ColoredAccordionItem(title='Item 1', color=(1, 1, 1, 0))
        item1.add_widget(Label(text='Content of Item 1'))
        accordion.add_widget(item1)

        item2 = ColoredAccordionItem(title='Item 2', color=(0, 1, 0, 1))
        item2.add_widget(Label(text='Content of Item 2'))
        accordion.add_widget(item2)

        item3 = ColoredAccordionItem(title='Item 3', color=(0, 0, 1, 1))
        item3.add_widget(Label(text='Content of Item 3'))
        accordion.add_widget(item3)

        return accordion

if __name__ == '__main__':
    MyApp().run()