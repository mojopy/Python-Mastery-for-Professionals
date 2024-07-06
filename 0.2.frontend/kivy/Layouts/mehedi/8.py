from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class NestedBoxLayoutApp(App):
    def build(self):
        # Outer BoxLayout (Vertical)
        outer_box = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Inner BoxLayout 1 (Horizontal)
        inner_box1 = BoxLayout(orientation='horizontal', padding=5, spacing=5)
        inner_box1.add_widget(Label(text='Inner Box 1 - Label 1'))
        inner_box1.add_widget(Button(text='Inner Box 1 - Button 1'))
        inner_box1.add_widget(Button(text='Inner Box 1 - Button 2'))

        # Inner BoxLayout 2 (Horizontal)
        inner_box2 = BoxLayout(orientation='horizontal', padding=5, spacing=5)
        inner_box2.add_widget(Label(text='Inner Box 2 - Label 1'))
        inner_box2.add_widget(Button(text='Inner Box 2 - Button 1'))
        inner_box2.add_widget(Button(text='Inner Box 2 - Button 2'))

        # Adding inner boxes to the outer box
        outer_box.add_widget(inner_box1)
        outer_box.add_widget(Label(text='Label between inner boxes'))
        outer_box.add_widget(inner_box2)

        return outer_box

if __name__ == '__main__':
    NestedBoxLayoutApp().run()
