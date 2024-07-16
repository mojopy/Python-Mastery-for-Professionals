import flet as ft

def main(page: ft.Page):
    page.title = "Enhanced Flet App"

    def button_clicked(e):
        lbl.value = f"You typed: {input_field.value}"
        page.update()

    def clear_button_clicked(e):
        input_field.value = ""
        lbl.value = ""
        page.update()

    lbl = ft.Text(value="Type something and click the button")
    input_field = ft.TextField(hint_text="Type here")
    btn = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    clear_btn = ft.ElevatedButton(text="Clear", on_click=clear_button_clicked)

    page.add(input_field, btn, clear_btn, lbl)

ft.app(target=main)
