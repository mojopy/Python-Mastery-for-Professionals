from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window

class MyBoxLayoutApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        # Create a BoxLayout with vertical orientation
        layout = BoxLayout(orientation='vertical', spacing=10, padding=[20, 10, 20, 10])
        
        # Create buttons with different size hints
        button1 = Button(text='Button 1', size_hint=(1, 0.2))
        button2 = Button(text='Button 2', size_hint=(1, 0.3))
        button3 = Button(text='Button 3', size_hint=(1, 0.5))
        
        # Add buttons to the layout
        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)
        
        return layout

if __name__ == '__main__':
    MyBoxLayoutApp().run()
