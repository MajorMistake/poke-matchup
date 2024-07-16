import reflex as rx

from ..components import nav_bar

def about() -> rx.Component:
    return rx.fragment(
        nav_bar(),
        "About"
    )