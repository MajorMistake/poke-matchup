import reflex as rx

from ..state import State, MakeTeam
from ..components import nav_bar, test_autocomplete, create_team_dialog

def detail() -> rx.Component:
    return rx.fragment(
        nav_bar(),
        rx.heading(MakeTeam.autocomplete_pokemon),
        rx.foreach(
            MakeTeam.autocomplete_pokemon, test_autocomplete
            ),
        create_team_dialog(),
        rx.button("Clicky", on_click=MakeTeam.toggleDialog)
    )