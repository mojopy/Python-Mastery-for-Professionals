from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 3  # Number of columns

        # Adding a label that spans 2 columns
        label = Label(text="This label spans 2 columns", size_hint_x=None, width=200)
        self.add_widget(label, index=len(self.children))

        # Adding a button
        self.add_widget(Button(text="Button 1"))
        self.add_widget(Button(text="Button 2"))

        # Adding another label
        self.add_widget(Label(text="Another label"))

        # Adding a button that spans 2 columns
        button = Button(text="This button spans 2 columns", size_hint_x=None, width=400)
        self.add_widget(button, index=len(self.children))

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    MyApp().run()
