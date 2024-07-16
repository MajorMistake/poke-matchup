import reflex as rx

from ..state import State
from ..state import Pokemon, Team

def poke_card(pokemon: Pokemon) -> rx.Component:
    return rx.card(
        rx.heading(pokemon.pokemon_name)
    )

def poke_list(team: Team) -> rx.Component:
    return rx.flex(
        rx.foreach(team.members, poke_card),
        wrap="wrap",
        spacing="2",
        padding=".25em"
    )

def team_card(team: Team) -> rx.Component:
    return rx.context_menu.root(
        rx.context_menu.trigger(
            rx.card(
                rx.heading(team.team_name),
                poke_list(team=team),
            ),
        ),
        rx.context_menu.content(
            rx.context_menu.item("Copy"),
            rx.context_menu.item("Compare"),
            rx.context_menu.item("Edit"),
            rx.context_menu.separator(),
            rx.context_menu.item("Delete", color="red"),
        ),
    )

def team_list() -> rx.Component:
    return rx.flex(
        rx.foreach(State.teamsObj, team_card),
        rx.spacer(),
        rx.button(
            "Create Team", type="submit",
            on_click=State.save_team(
                Team.create_team(
                    name="Big Bois",
                    members=[Pokemon.create_poke("snorlax")]
                    )
                )
            ),
        direction="column",
        spacing="3",
        min_width="10em",
        padding="1em"
    )

def test_autocomplete(name: str) -> rx.Component:
    return rx.card(
        rx.text(name)
    )