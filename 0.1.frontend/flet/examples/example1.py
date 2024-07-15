import flet as ft

def main(page: ft.Page):
    page.title = "Simple Flet App"

    def button_clicked(e):
        txt.value = "Button clicked!"
        page.update()

    txt = ft.Text(value="Hello, Flet!")
    btn = ft.ElevatedButton(text="Click me", on_click=button_clicked)

    page.add(txt, btn)

ft.app(target=main)