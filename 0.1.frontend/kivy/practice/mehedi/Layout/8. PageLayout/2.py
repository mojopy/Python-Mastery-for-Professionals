from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = PageLayout()

        page1 = Button(text='Page 1: Button 1', font_size='20sp')
        page2 = Button(text='Page 2: Button 2', font_size='20sp')
        page3 = Button(text='Page 3: Button 3', font_size='20sp')

        layout.add_widget(page1)
        layout.add_widget(page2)
        layout.add_widget(page3)

        return layout

if __name__ == '__main__':
    MyApp().run()
