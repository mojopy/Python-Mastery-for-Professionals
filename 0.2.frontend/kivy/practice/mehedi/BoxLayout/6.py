from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class NestedBoxLayoutApp(App):
    def build(self):
        # Outer BoxLayout (Vertical)
        outer_box = BoxLayout(orientation='vertical')

        # Inner BoxLayout (Horizontal)
        inner_box = BoxLayout(orientation='horizontal')
        inner_box.add_widget(Button(text='Button 1'))
        inner_box.add_widget(Button(text='Button 2'))
        inner_box.add_widget(Button(text='Button 3'))

        # Add widgets to the outer BoxLayout
        outer_box.add_widget(Label(text='Label above inner box'))
        outer_box.add_widget(inner_box)
        outer_box.add_widget(Label(text='Label below inner box'))

        return outer_box

if __name__ == '__main__':
    NestedBoxLayoutApp().run()
