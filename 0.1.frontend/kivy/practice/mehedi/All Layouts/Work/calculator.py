from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.operators = ['+', '-', '*', '/']
        self.last_was_operator = False
        self.last_button = None

        # Set up the layout
        layout = GridLayout(cols=4, spacing=10, padding=10)

        # Add the display
        self.display = TextInput(
            multiline=False, readonly=True, halign="right", font_size=32
        )
        layout.add_widget(self.display)
        
        # Add buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '.', '0', 'C', '+'
        ]
        for button in buttons:
            layout.add_widget(Button(text=button, on_press=self.on_button_press))

        # Add the Equals button
        equals_button = Button(text='=', pos_hint={"center_x": 0.5, "center_y": 0.5})
        equals_button.bind(on_press=self.on_solution)
        layout.add_widget(equals_button)

        return layout

    def on_button_press(self, instance):
        current = self.display.text
        button_text = instance.text

        if button_text == 'C':
            self.display.text = ''
        elif button_text in self.operators:
            if current and (self.last_was_operator is False):
                self.display.text += button_text
                self.last_was_operator = True
        else:
            if current == '' and button_text == '0':
                return
            self.display.text += button_text
            self.last_was_operator = False

    def on_solution(self, instance):
        text = self.display.text
        try:
            # Evaluate the expression
            solution = str(eval(text))
            self.display.text = solution
        except Exception:
            self.display.text = "Error"

if __name__ == "__main__":
    CalculatorApp().run()
