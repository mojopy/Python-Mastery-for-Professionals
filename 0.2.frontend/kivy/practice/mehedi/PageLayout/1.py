from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        layout = PageLayout()

        page1 = Label(text='Page 1', font_size='40sp')
        page2 = Label(text='Page 2', font_size='40sp')
        page3 = Label(text='Page 3', font_size='40sp')

        layout.add_widget(page1)
        layout.add_widget(page2)
        layout.add_widget(page3)

        return layout

if __name__ == '__main__':
    MyApp().run()
