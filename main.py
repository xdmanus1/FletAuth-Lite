import flet as ft
from flet.security import encrypt, decrypt

secret_key = "S3CreT!"


def main(page: ft.Page):
    page.title = "Flet Navigation Example"
    page.adaptive = True

    # Initialize references
    nav_bar = ft.Ref[ft.NavigationBar]()
    email_ref = ft.Ref[ft.TextField]()
    password_ref = ft.Ref[ft.TextField]()

    # Encrypt credentials for testing
    Testemail = encrypt("Test", secret_key)
    Testpass = encrypt("Test", secret_key)

    # Fonts
    page.fonts = {
        "Anta": "./assets/fonts/Anta-Regular.ttf",
    }
    # Track login state
    user_logged_in = False

    def handle_submit(e):
        nonlocal user_logged_in
        # Capture the values entered by the user
        email = email_ref.current.value
        password = password_ref.current.value
        DecryptedEmail = decrypt(Testemail, secret_key)
        DecryptedPass = decrypt(Testpass, secret_key)

        # Check credentials
        if email == DecryptedEmail and password == DecryptedPass:
            user_logged_in = True
            update_navigation_bar()
            page.go("/3")
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Invalid credentials"))
            page.snack_bar.open = True
            page.update()

    def update_navigation_bar():
        if nav_bar.current is not None:
            # Rebuild the navigation bar with an additional destination if logged in
            destinations = [
                ft.NavigationDestination(icon=ft.icons.HOME, label="Home"),
                ft.NavigationDestination(icon=ft.icons.SETTINGS, label="Settings"),
                ft.NavigationDestination(icon=ft.icons.LOGIN, label="Login"),
            ]
            if user_logged_in:
                destinations.append(
                    ft.NavigationDestination(icon=ft.icons.PERSON, label="Profile")
                )
            nav_bar.current.destinations = destinations
            page.update()

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(
                        title=ft.Text("Flet Navigation", font_family="Anta"),
                        bgcolor=ft.colors.SURFACE_VARIANT,
                    ),
                    ft.NavigationBar(
                        ref=nav_bar,
                        destinations=[],  # Start with empty destinations
                        on_change=lambda e: page.go(f"/{e.control.selected_index}"),
                    ),
                ],
            )
        )

        if page.route == "/0" or page.route == "/":
            nav_bar.current.selected_index = 0
            page.views[-1].controls.insert(1, ft.Text("Home Page"))
        elif page.route == "/1":
            nav_bar.current.selected_index = 1
            page.views[-1].controls.insert(1, ft.Text("Settings Page"))
        elif page.route == "/2":
            nav_bar.current.selected_index = 2
            page.views[-1].controls.insert(
                1,
                # Center
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Text("Login", size=30, font_family="Anta"),
                                ft.TextField(
                                    ref=email_ref,
                                    label="Email",
                                    border_radius=100,
                                    width=400,
                                ),
                                ft.TextField(
                                    ref=password_ref,
                                    password=True,
                                    can_reveal_password=True,
                                    label="Password",
                                    border_radius=100,
                                    width=400,
                                ),
                                ft.ElevatedButton("Submit", on_click=handle_submit),
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

        elif page.route == "/3":
            nav_bar.current.selected_index = 3
            page.views[-1].controls.insert(
                1,
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Text("Hello", size=50, font_family="Anta"),
                                ft.Text(value=decrypt(Testemail, secret_key)),
                            ],
                        )
                    ],
                    expand=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            )

        # Update the navigation bar after it has been initialized
        update_navigation_bar()
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)
