import kivy
from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        layout = PageLayout()

        # Add pages to the page layout
        page1 = Button(text='Page 1')
        page2 = Label(text='Page 2')
        page3 = Button(text='Page 3')

        layout.add_widget(page1)
        layout.add_widget(page2)
        layout.add_widget(page3)

        return layout

if __name__ == '__main__':
    MyApp().run()
