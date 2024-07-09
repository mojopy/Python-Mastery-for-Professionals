import kivy
from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle

class MyApp(App):
    def build(self):
        layout = PageLayout()

        # Page 1 with a Button
        page1 = BoxLayout()
        with page1.canvas.before:
            Color(1, 0, 0, 1)  # Red background
            self.rect = Rectangle(size=page1.size, pos=page1.pos)
            page1.bind(size=self._update_rect, pos=self._update_rect)
        button1 = Button(text='Page 1', size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        page1.add_widget(button1)
        
        # Page 2 with a Label
        page2 = BoxLayout()
        with page2.canvas.before:
            Color(0, 1, 0, 1)  # Green background
            self.rect = Rectangle(size=page2.size, pos=page2.pos)
            page2.bind(size=self._update_rect, pos=self._update_rect)
        label2 = Label(text='Page 2', size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        page2.add_widget(label2)
        
        # Page 3 with a Button
        page3 = BoxLayout()
        with page3.canvas.before:
            Color(0, 0, 1, 1)  # Blue background
            self.rect = Rectangle(size=page3.size, pos=page3.pos)
            page3.bind(size=self._update_rect, pos=self._update_rect)
        button3 = Button(text='Page 3', size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        page3.add_widget(button3)
        
        # Add pages to the page layout
        layout.add_widget(page1)
        layout.add_widget(page2)
        layout.add_widget(page3)

        return layout

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

if __name__ == '__main__':
    MyApp().run()
