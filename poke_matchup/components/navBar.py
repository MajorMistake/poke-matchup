import reflex as rx

def nav_bar() -> rx.hstack:
    return rx.hstack(
    rx.hstack(
        rx.heading("Pokemon Compare!", font_size="2em"),
        rx.color_mode.button(position="bottom-right"),
    ),
    rx.spacer(),
    rx.menu.root(
        rx.menu.trigger(
            rx.button("Menu"),
        ),
        rx.menu.content(
            rx.menu.item(rx.link("Home", href="/")),
            rx.menu.item(rx.link("Compare", href="comparison")),
            rx.menu.item(rx.link("Detail", href="detail")),
            rx.menu.item(rx.link("About", href="about")),
            width="10em",
        ),
    ),
    top="0px",
    padding="1em",
    height="4em",
    width="100%",
)