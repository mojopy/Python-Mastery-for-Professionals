from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = PageLayout()

        # Page 1 with ScrollView
        scroll_view1 = ScrollView()
        content1 = BoxLayout(orientation='vertical', size_hint_y=None)
        content1.bind(minimum_height=content1.setter('height'))
        for i in range(20):
            content1.add_widget(Label(text=f'Page 1: Item {i+1}', size_hint_y=None, height=40))
        scroll_view1.add_widget(content1)
        layout.add_widget(scroll_view1)

        # Page 2 with ScrollView
        scroll_view2 = ScrollView()
        content2 = BoxLayout(orientation='vertical', size_hint_y=None)
        content2.bind(minimum_height=content2.setter('height'))
        for i in range(20):
            content2.add_widget(Label(text=f'Page 2: Item {i+1}', size_hint_y=None, height=40))
        scroll_view2.add_widget(content2)
        layout.add_widget(scroll_view2)

        # Page 3 with ScrollView
        scroll_view3 = ScrollView()
        content3 = BoxLayout(orientation='vertical', size_hint_y=None)
        content3.bind(minimum_height=content3.setter('height'))
        for i in range(20):
            content3.add_widget(Label(text=f'Page 3: Item {i+1}', size_hint_y=None, height=40))
        scroll_view3.add_widget(content3)
        layout.add_widget(scroll_view3)

        return layout

if __name__ == '__main__':
    MyApp().run()
