import flet as ft

def main(page: ft.Page):
    page.title = "Interactive Card Example"

    def change_song(e):
        title.value = "Stairway to Heaven"
        subtitle.value = "Led Zeppelin - 1971"
        page.update()

    def toggle_favorite(e):
        icon.name = ft.icons.FAVORITE if icon.name == ft.icons.FAVORITE_BORDER else ft.icons.FAVORITE_BORDER
        icon.color = "red" if icon.name == ft.icons.FAVORITE else None
        page.update()

    icon = ft.Icon(ft.icons.FAVORITE_BORDER)
    title = ft.Text("The Enchanted Nightingale")
    subtitle = ft.Text("Music by Julie Gable. Lyrics by Sidney Stein.")

    card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=icon,
                        title=title,
                        subtitle=subtitle,
                        on_click=toggle_favorite,
                    ),
                    ft.Row(
                        [
                            ft.ElevatedButton("Change Song", on_click=change_song),
                            ft.ElevatedButton("Play", on_click=lambda _: page.show_snack_bar(
                                ft.SnackBar(content=ft.Text("Playing song..."))
                            )),
                        ],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ]
            ),
            width=400,
            padding=10,
        )
    )
    
    page.add(card)

ft.app(target=main)