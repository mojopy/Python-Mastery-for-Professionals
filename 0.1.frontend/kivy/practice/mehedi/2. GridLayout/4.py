from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class SizeGridLayoutApp(App):
    def build(self):
        # Create a GridLayout with 3 columns and 2 rows
        layout = GridLayout(cols=3, row_force_default=True,
        row_default_height=40, col_force_default=True,
        col_default_width=100)

        # Add widgets to the layout
        layout.add_widget(Label(text='Label 1'))
        layout.add_widget(Button(text='Button 1'))
        layout.add_widget(Button(text='Button 2'))
        layout.add_widget(Label(text='Label 2'))
        layout.add_widget(Label(text='Label 3'))
        layout.add_widget(Button(text='Button 3'))

        return layout

if __name__ == '__main__':
    SizeGridLayoutApp().run()
