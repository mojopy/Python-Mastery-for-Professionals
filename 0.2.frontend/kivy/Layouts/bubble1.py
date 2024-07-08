import kivy
from kivy.app import App
from kivy.uix.bubble import Bubble, BubbleButton
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class MyApp(App):
    def build(self):
        layout = FloatLayout()

        # Create a button that will show the bubble when clicked
        main_button = Button(text='Show Bubble', size_hint=(None, None), size=(150, 50), pos=(300, 400))
        main_button.bind(on_release=self.show_bubble)
        layout.add_widget(main_button)

        return layout

    def show_bubble(self, instance):
        # Create a bubble
        bubble = Bubble(arrow_pos='top_mid')

        # Add bubble buttons
        btn1 = BubbleButton(text='Option 1')
       

        bubble.add_widget(btn1)
    

        # Set the position of the bubble relative to the button
        bubble.pos = (instance.x - bubble.width / 2 + instance.width / 2, instance.y - bubble.height)
        instance.parent.add_widget(bubble)

if __name__ == '__main__':
    MyApp().run()
