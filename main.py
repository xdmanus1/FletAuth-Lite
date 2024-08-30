import flet as ft


def main(page: ft.Page):
    page.title = "Flet Navigation Example"
    nav_bar = ft.Ref[ft.NavigationBar]()

    page.fonts = {
        "SUSE": "./assets/fonts/Anta-Regular.ttf",
    }

    def handle_close(e):
        page.close(dlg_modal)

    def close_banner(e):
        page.close(banner)
        page.add(ft.Text("Action clicked: " + e.control.text))

    action_button_style = ft.ButtonStyle(color=ft.colors.BLUE)

    banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
        content=ft.Text(
            value="Oops, there were some errors while trying to delete the file. What would you like me to do?",
            color=ft.colors.BLACK,
        ),
        actions=[
            ft.TextButton(
                text="Retry", style=action_button_style, on_click=close_banner
            ),
            ft.TextButton(
                text="Ignore", style=action_button_style, on_click=close_banner
            ),
            ft.TextButton(
                text="Cancel", style=action_button_style, on_click=close_banner
            ),
        ],
    )

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Please confirm"),
        content=ft.Text("Do you really want to delete all those files?"),
        actions=[
            ft.TextButton("Yes", on_click=handle_close),
            ft.TextButton("No", on_click=handle_close),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: page.add(
            ft.Text("Modal dialog dismissed"),
        ),
    )

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(
                        title=ft.Text("Flet Navigation", font_family="SUSE"),
                        bgcolor=ft.colors.SURFACE_VARIANT,
                    ),
                    ft.NavigationBar(
                        ref=nav_bar,
                        destinations=[
                            ft.NavigationDestination(icon=ft.icons.HOME, label="Home"),
                            ft.NavigationDestination(
                                icon=ft.icons.SETTINGS,
                                label="Settings",
                                selected_icon=ft.icons.SETTINGS_ACCESSIBILITY_ROUNDED,
                            ),
                            ft.NavigationDestination(
                                icon=ft.icons.LOGIN, label="Login"
                            ),
                        ],
                        on_change=lambda e: page.go(f"/{e.control.selected_index}"),
                    ),
                ],
            )
        )

        if page.route == "/0" or page.route == "/":
            nav_bar.current.selected_index = 0
            page.views[-1].controls.insert(
                1,
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Text("Home Page"),
                                ft.ElevatedButton(
                                    "Home Page", on_click=lambda e: page.open(dlg_modal)
                                ),
                                ft.DataTable(
                                    columns=[
                                        ft.DataColumn(
                                            ft.Text("Date"),
                                        ),
                                        ft.DataColumn(
                                            ft.Text("Inside Temp"), numeric=True
                                        ),
                                        ft.DataColumn(
                                            ft.Text("Outside Temp"), numeric=True
                                        ),
                                    ],
                                    rows=[
                                        ft.DataRow(
                                            cells=[
                                                ft.DataCell(ft.Text("00:11")),
                                                ft.DataCell(ft.Text("18")),
                                                ft.DataCell(ft.Text("20")),
                                            ],
                                        ),
                                        ft.DataRow(
                                            cells=[
                                                ft.DataCell(ft.Text("00:15")),
                                                ft.DataCell(ft.Text("20")),
                                                ft.DataCell(ft.Text("23")),
                                            ],
                                        ),
                                        ft.DataRow(
                                            cells=[
                                                ft.DataCell(ft.Text("00:21")),
                                                ft.DataCell(ft.Text("23")),
                                                ft.DataCell(ft.Text("25")),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        )
                    ],
                    expand=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            )
        elif page.route == "/1":
            nav_bar.current.selected_index = 1
            page.views[-1].controls.insert(
                1,
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Text("Settings Page"),
                                ft.ElevatedButton(
                                    "Home Page", on_click=lambda e: page.open(dlg_modal)
                                ),
                                ft.TextField(
                                    password=False,
                                    label="Email",
                                    border_radius=100,
                                    focused_border_color=ft.colors.DEEP_ORANGE_500,
                                ),
                                ft.TextField(
                                    password=True,
                                    can_reveal_password=True,
                                    label="Password",
                                    border_radius=100,
                                ),
                                ft.ElevatedButton(
                                    on_click=lambda e: page.open(banner),
                                    content=ft.Row(
                                        [
                                            ft.Icon(name=ft.icons.SEND, color="red"),
                                            ft.Text("Submit"),
                                        ],
                                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                    ),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        )
                    ],
                    expand=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            )
        elif page.route == "/2":
            nav_bar.current.selected_index = 2
            page.views[-1].controls.insert(
                1,
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Text("Login", size=30, font_family="SUSE"),
                                ft.TextField(
                                    password=False,
                                    label="Email",
                                    border_radius=100,
                                    focused_border_color=ft.colors.DEEP_ORANGE_500,
                                ),
                                ft.TextField(
                                    password=True,
                                    can_reveal_password=True,
                                    label="Password",
                                    border_radius=100,
                                ),
                                ft.ElevatedButton(
                                    on_click=lambda e: page.open(banner),
                                    content=ft.Row(
                                        [
                                            ft.Icon(name=ft.icons.SEND, color="red"),
                                            ft.Text("Submit"),
                                        ],
                                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                    ),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        )
                    ],
                    expand=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            )

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)
