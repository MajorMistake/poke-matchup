import reflex as rx

from ..state import State, MakeTeam
from .misc import poke_card

def create_team_dialog() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title("Create a Team!"),
            rx.dialog.description("Here's the form:"),
            rx.form(
                rx.input(
                    placeholder="Team Name",
                    name="team_name"
                    ),
                rx.text("Team Members:"),
                rx.foreach(
                    State.activePokemon, poke_card
                    ),
                rx.hstack(
                    rx.input(
                        placeholder="Add Pokemon",
                        name="new_poke",
                        on_change=MakeTeam.set_pokeInput
                        ),
                    rx.button(
                        "+",
                        on_click=MakeTeam.possible_pokemon
                        ),
                    ),
                rx.button("Save Team", type="submit"),
                reset_on_submit=True,
                ),
            rx.dialog.close(
                rx.button("Exit", color="red",),
                ),
            ),
            open=MakeTeam.openDialog
        )