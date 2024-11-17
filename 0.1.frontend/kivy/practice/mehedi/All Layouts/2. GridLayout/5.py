from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class NestedGridLayoutApp(App):
    def build(self):
        # Outer GridLayout with 1 column
        outer_layout = GridLayout(cols=1)

        # Inner GridLayout with 2 columns
        inner_layout = GridLayout(cols=2)
        inner_layout.add_widget(Label(text='Inner Label 1'))
        inner_layout.add_widget(Button(text='Inner Button 1'))
        inner_layout.add_widget(Label(text='Inner Label 2'))
        inner_layout.add_widget(Button(text='Inner Button 2'))

        # Add widgets to the outer layout
        outer_layout.add_widget(Label(text='Outer Label 1'))
        outer_layout.add_widget(inner_layout)
        outer_layout.add_widget(Label(text='Outer Label 2'))

        return outer_layout

if __name__ == '__main__':
    NestedGridLayoutApp().run()
