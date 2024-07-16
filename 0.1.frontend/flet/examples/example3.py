import flet as ft

def main(page: ft.Page):
    page.title = "Enhanced Flet App with More Features"

    # Counter for button clicks
    click_counter = 0

    def update_text():
        lbl.value = f"You typed: {input_field.value} (Clicked {click_counter} times)"
        lbl.color = color_picker.value
        lbl.size = text_size_slider.value
        lbl.weight = "bold" if bold_checkbox.value else "normal"
        page.update()

    def button_clicked(e):
        nonlocal click_counter
        click_counter += 1
        update_text()

    def clear_button_clicked(e):
        nonlocal click_counter
        input_field.value = ""
        lbl.value = ""
        click_counter = 0
        page.update()

    lbl = ft.Text(value="Type something and click the button")
    input_field = ft.TextField(hint_text="Type here")
    btn = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    clear_btn = ft.ElevatedButton(text="Clear", on_click=clear_button_clicked)

    color_picker = ft.Dropdown(
        options=[
            ft.dropdown.Option("black"),
            ft.dropdown.Option("red"),
            ft.dropdown.Option("blue"),
            ft.dropdown.Option("green"),
        ],
        value="black",
    )

    text_size_slider = ft.Slider(min=10, max=30, value=16)
    bold_checkbox = ft.Checkbox(label="Bold Text", value=False)

    page.add(
        ft.Row([input_field, btn, clear_btn]),
        ft.Row([color_picker, text_size_slider, bold_checkbox]),
        lbl
    )

ft.app(target=main)

