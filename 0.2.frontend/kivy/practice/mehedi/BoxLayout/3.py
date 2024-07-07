from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        top_layout = BoxLayout(orientation='horizontal')
        btn1 = Button(text='Top Button 1')
        btn2 = Button(text='Top Button 2')
        top_layout.add_widget(btn1)
        top_layout.add_widget(btn2)
        
        middle_layout = BoxLayout(orientation='horizontal')
        btn3 = Button(text='Middle Button 1')
        btn4 = Button(text='Middle Button 2')
        middle_layout.add_widget(btn3)
        middle_layout.add_widget(btn4)

        bottom_layout = BoxLayout(orientation='horizontal')
        btn5 = Button(text='Bottom Button 1')
        btn6 = Button(text='Bottom Button 2')
        bottom_layout.add_widget(btn5)
        bottom_layout.add_widget(btn6)

        main_layout.add_widget(top_layout)
        main_layout.add_widget(middle_layout)
        main_layout.add_widget(bottom_layout)

        return main_layout

if __name__ == '__main__':
    MyApp().run()
