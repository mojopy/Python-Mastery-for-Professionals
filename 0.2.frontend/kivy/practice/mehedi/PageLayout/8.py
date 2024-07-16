from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = PageLayout()

        def switch_to_page1(instance):
            layout.page = 0

        def switch_to_page2(instance):
            layout.page = 1

        def switch_to_page3(instance):
            layout.page = 2

        # Page 1
        page1 = BoxLayout(orientation='vertical')
        page1.add_widget(Label(text='Page 1', font_size='30sp'))
        button_to_page2 = Button(text='Go to Page 2')
        button_to_page2.bind(on_release=switch_to_page2)
        page1.add_widget(button_to_page2)
        layout.add_widget(page1)

        # Page 2
        page2 = BoxLayout(orientation='vertical')
        page2.add_widget(Label(text='Page 2', font_size='30sp'))
        button_to_page1 = Button(text='Go to Page 1')
        button_to_page1.bind(on_release=switch_to_page1)
        page2.add_widget(button_to_page1)
        button_to_page3 = Button(text='Go to Page 3')
        button_to_page3.bind(on_release=switch_to_page3)
        page2.add_widget(button_to_page3)
        layout.add_widget(page2)

        # Page 3
        page3 = BoxLayout(orientation='vertical')
        page3.add_widget(Label(text='Page 3', font_size='30sp'))
        button_to_page2 = Button(text='Go to Page 2')
        button_to_page2.bind(on_release=switch_to_page2)
        page3.add_widget(button_to_page2)
        layout.add_widget(page3)

        return layout

if __name__ == '__main__':
    MyApp().run()
