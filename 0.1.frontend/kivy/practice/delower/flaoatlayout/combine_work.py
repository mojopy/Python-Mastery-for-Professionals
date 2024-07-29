from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image 
from kivy.uix.slider import Slider
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput

class ToggleButtonApp(App):
    def build(self):
        layout = FloatLayout()

        imeage = Image(source="path_to_your_image.png",size_hint=(.4,.28), pos_hint={"x":.3,"y":.7})
        layout.add_widget(imeage)

        self.labe = Label(text="You Typed :",size_hint=(.1, .1),pos_hint={'x': .8, 'y': .9})
        layout.add_widget(self.labe)
        
        self.text_input = TextInput(hint_text='Type Comments',size_hint=(.4, .1),pos_hint={'x': .3, 'y': .59})
        self.text_input.bind(text=self.on_text_change)

        self.label_text = Label(text="Volume : 0",size_hint=(.3, .1),pos_hint={'x': .02, 'y': .5})
        layout.add_widget(self.label_text)
        
        self.label_hello = Label(text="Checkbox is unchecked",size_hint=(.4, .1),pos_hint={'x': .65, 'y': .6})
        layout.add_widget(self.label_hello)
        
        checkbox = CheckBox(size_hint=(.1, .1),pos_hint={'x': .8, 'y': .5})
        checkbox.bind(active=self.on_checkbox_active)
        layout.add_widget(checkbox)


        slider = Slider(min=0, max=100, value=0,size_hint=(.8, .1),pos_hint={'x': .1, 'y': .4})
        slider.bind(value=self.on_value_change)
        layout.add_widget(slider)

        layout.add_widget(self.text_input)
        self.label = Label(text="Toggle Button is Off", size_hint=(.2, .1), pos_hint={"x":.05, "y":.8})
        layout.add_widget(self.label)



        toggle_Button = ToggleButton(text="Toggle Me", size_hint=(.2, .1), pos_hint={"x":.05, "y":.7})
        toggle_Button.bind(on_press = self.On_Chanage_text)
        layout.add_widget(toggle_Button)

        return layout

    def On_Chanage_text(self, toggle_Button):
        if toggle_Button.state == "down":
            self.label.text="Toggle Button is on"
        else:
            self.label.text="Toggle Button is off"

    def on_text_change(self, instance, value):
        self.labe.text = f"Your comments is  :  {value}"

    def on_value_change(self, instance, value):
        self.label_text.text = f"Volume : {int(value)}"

    def on_checkbox_active(self, checkbox, value):
        if value:
            self.label_hello.text = "Checkbox is checked"
        else:
            self.label_hello.text = "Checkbox is unchecked"
        

if __name__=="__main__":
    ToggleButtonApp().run()