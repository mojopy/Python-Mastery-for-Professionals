import flet as ft

def main(page: ft.Page):
    page.title = "Card Layout Example"

    # Create a card
    card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("Card Title", style="headlineSmall"),
                    ft.Text("This is a description of the card."),
                    ft.ElevatedButton("Action", on_click=lambda _: print("Button clicked!"))
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=10
            ),
            padding=10,
            width=300,
            height=200,
            border_radius=10,
            bgcolor=ft.colors.WHITE,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=10,
                color=ft.colors.GREY
            )
        )
    )

    # Add card to the page
    page.add(card)

ft.app(target=main)
