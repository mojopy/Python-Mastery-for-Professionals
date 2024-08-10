from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", spacing = 10, padding = 10)

        layout1 = BoxLayout(orientation="horizontal")
        layout1.add_widget(Button(text="Top Button 1"))
        layout1.add_widget(Button(text="Top Button 2"))

        layout2 = BoxLayout(orientation="horizontal")
        layout2.add_widget(Button(text="Middlw Button 1"))
        layout2.add_widget(Button(text="Middle Button 2"))

        layout3 = BoxLayout(orientation="horizontal")
        layout3.add_widget(Button(text="Bottom Button 3"))
        layout3.add_widget(Button(text="Bottom Button 3"))

        layout.add_widget(layout1)
        layout.add_widget(layout2)
        layout.add_widget(layout3)

        return layout 

if __name__=="__main__":
    MyApp().run()