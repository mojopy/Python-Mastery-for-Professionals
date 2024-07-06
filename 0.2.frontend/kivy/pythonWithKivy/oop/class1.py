
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class Enemy:
    def __init__(self):
        self.life = 3

    def attack(self):
        print("ouch!")
        self.life -= 1

    def check_life(self):
        if self.life <= 0:
            return "I am dead"
        else:
            return f"I am alive and I have {self.life} life"

    def set_life(self, new_life):
        self.life = new_life


class MyApp(App):
    def build(self):
        self.enemy = Enemy()

        self.layout = BoxLayout(orientation='vertical')

        self.input = TextInput(text='', multiline=False, hint_text="Enter new life value")
        self.layout.add_widget(self.input)

        self.label = Label(text=self.enemy.check_life())
        self.layout.add_widget(self.label)

        self.attack_button = Button(text='Attack')
        self.attack_button.bind(on_press=self.attack_enemy)
        self.layout.add_widget(self.attack_button)

        self.check_button = Button(text='Check Life')
        self.check_button.bind(on_press=self.check_enemy_life)
        self.layout.add_widget(self.check_button)

        self.set_life_button = Button(text='Set Life')
        self.set_life_button.bind(on_press=self.set_enemy_life)
        self.layout.add_widget(self.set_life_button)

        return self.layout

    def attack_enemy(self, instance):
        self.enemy.attack()
        self.label.text = self.enemy.check_life()

    def check_enemy_life(self, instance):
        self.label.text = self.enemy.check_life()

    def set_enemy_life(self, instance):
        try:
            new_life = int(self.input.text)
            self.enemy.set_life(new_life)
            self.label.text = self.enemy.check_life()
        except ValueError:
            self.label.text = "Invalid input! Please enter an integer."


if __name__ == '__main__':
    MyApp().run()
