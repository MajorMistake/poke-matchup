import reflex as rx

from ..components import nav_bar, team_list

def index() -> rx.Component:
    return rx.fragment(
        rx.vstack(
            nav_bar(),
            rx.box(
                team_list(),
                margin="auto",
                width="50%"
            ),
            spacing="5",
            min_height="85vh",
        ),
    )