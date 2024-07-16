from kivy.app import App
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        accordion = Accordion()

        item1 = AccordionItem(title='Item 1')
        item1.add_widget(Label(text='Content of Item 1'))
        accordion.add_widget(item1)

        item2 = AccordionItem(title='Item 2')
        item2.add_widget(Label(text='Content of Item 2'))
        accordion.add_widget(item2)

        item3 = AccordionItem(title='Item 3')
        item3.add_widget(Label(text='Content of Item 3'))
        accordion.add_widget(item3)

        return accordion

if __name__ == '__main__':
    MyApp().run()
