from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class SpanGridLayoutApp(App):
    def build(self):
        # Create a GridLayout with 3 columns
        layout = GridLayout(cols=3)

        # Add widgets to the layout
        layout.add_widget(Label(text='Label 1'), index=0)
        layout.add_widget(Button(text='Button 1'), index=1)
        layout.add_widget(Button(text='Button 2'), index=2)
        layout.add_widget(Label(text='Label 2'), index=3)
        layout.add_widget(Label(text='Label 3'), index=4)
        layout.add_widget(Button(text='Button 3'), index=5)

        # Add a widget that spans multiple columns
        layout.add_widget(Button(text='Button spanning 3 columns'), index=6)

        return layout

if __name__ == '__main__':
    SpanGridLayoutApp().run()