import reflex as rx

from ..components import nav_bar

def comparison() -> rx.Component:
    return rx.fragment(
        nav_bar(),
        "Compare",
    )