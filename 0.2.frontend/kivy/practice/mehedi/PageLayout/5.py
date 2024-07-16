from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.image import Image

class MyApp(App):
    def build(self):
        layout = PageLayout()

        page1 = Image(source='image1.jpg')
        page2 = Image(source='image2.jpg')
        page3 = Image(source='image3.jpg')

        layout.add_widget(page1)
        layout.add_widget(page2)
        layout.add_widget(page3)

        return layout

if __name__ == '__main__':
    MyApp().run()
