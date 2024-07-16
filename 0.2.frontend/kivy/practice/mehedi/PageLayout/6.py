from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = PageLayout()

        # Page 1 with nested BoxLayout
        page1 = BoxLayout(orientation='vertical')
        page1.add_widget(Label(text='Page 1: Label', font_size='30sp'))
        page1.add_widget(Button(text='Page 1: Button'))
        layout.add_widget(page1)

        # Page 2 with nested BoxLayout
        page2 = BoxLayout(orientation='horizontal')
        page2.add_widget(Button(text='Page 2: Button 1'))
        page2.add_widget(Button(text='Page 2: Button 2'))
        layout.add_widget(page2)

        # Page 3 with nested BoxLayout
        page3 = BoxLayout(orientation='vertical')
        page3.add_widget(Label(text='Page 3: Label 1', font_size='30sp'))
        page3.add_widget(Label(text='Page 3: Label 2', font_size='20sp'))
        layout.add_widget(page3)

        return layout

if __name__ == '__main__':
    MyApp().run()
