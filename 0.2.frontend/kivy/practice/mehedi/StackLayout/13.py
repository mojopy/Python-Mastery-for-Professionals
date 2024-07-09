from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class DashboardExample(App):
    def build(self):
        layout = StackLayout(orientation='lr-tb', padding=10, spacing=10)

        for i in range(1, 5):
            panel = StackLayout(orientation='tb-rl', padding=5, spacing=5, size_hint=(None, None), size=(300, 300))
            panel.add_widget(Label(text=f'Panel {i}', size_hint=(None, None), size=(280, 40)))
            
            for j in range(4):
                btn = Button(text=f'Button {i}-{j+1}', size_hint=(None, None), size=(130, 50))
                panel.add_widget(btn)
            
            layout.add_widget(panel)
        
        return layout

if __name__ == '__main__':
    DashboardExample().run()
