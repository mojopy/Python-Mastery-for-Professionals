from kivy.app import App
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        accordion = Accordion()

        item1 = AccordionItem(title='Item 1', background_normal='', background_color=(1, 0, 0, 1))
        item1.add_widget(Label(text='Content of Item 1'))
        accordion.add_widget(item1)

        item2 = AccordionItem(title='Item 2', background_normal='', background_color=(0, 1, 0, 1))
        item2.add_widget(Label(text='Content of Item 2'))
        accordion.add_widget(item2)

        item3 = AccordionItem(title='Item 3', background_normal='', background_color=(0, 0, 1, 1))
        item3.add_widget(Label(text='Content of Item 3'))
        accordion.add_widget(item3)

        return accordion

if __name__ == '__main__':
    MyApp().run()
