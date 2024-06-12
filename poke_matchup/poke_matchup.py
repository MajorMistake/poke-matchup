import requests
import json

import reflex as rx

from typing import List

class Stats(rx.Base):
    stat_name: str
    value: int

class Pokemon(rx.Base):
    pokemon_name: str
    types: List[str]
    stats: List[Stats]
    abilities: List[str]
    moves: List[str]

    @staticmethod
    def create_poke(name: str):
        pokemon = {}
        r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
        pokeRaw = json.loads(r.text)
        pokemon["name"] = name
        
        pokeTypes = pokeRaw["types"]
        typeList = []
        for item in pokeTypes:
            typeList.append(item["type"]["name"]) 
        pokemon["types"] = typeList 

        pokeStats = pokeRaw["stats"] 
        stats = [] 
        for item in pokeStats: 
            stat_name = item["stat"]["name"] 
            value = item["base_stat"]
            statObj = Stats(stat_name=stat_name, value=value)
            stats.append(statObj) 
        pokemon["stats"] = stats 

        pokeAbilities = pokeRaw["abilities"] 
        abilities = [] 
        for item in pokeAbilities: 
            abilities.append(item["ability"]["name"]) 
        pokemon["abilities"]= abilities 

        pokeMoves = pokeRaw["moves"] 
        moves = [] 
        for item in pokeMoves: 
            moves.append(item["move"]["name"]) 
        pokemon["moves"] = moves 

        created_pokemon = Pokemon(pokemon_name=pokemon["name"], types=pokemon["types"], stats=pokemon["stats"],
                                  abilities=pokemon["abilities"], moves=pokemon["moves"])

        return created_pokemon

class Team(rx.Base):
    team_name: str
    members: List[Pokemon]
    
    @staticmethod
    def create_team(name: str, members: List[Pokemon]): 
        created_team = Team(team_name=name, members=members)
        return created_team

    def add_teammate(self, pokemon: Pokemon) -> None: 
        self.members.append(pokemon)

    def remove_teammate(self, pokemon: Pokemon) -> None: 
        if pokemon in self.members: 
            self.members.remove(pokemon) 
        else: print(f"ERROR: {pokemon.pokemon_name} not found.") 

class State(rx.State):
    teamsObj : List[Team] = [
        Team.create_team(name="Team Titans", members=[Pokemon.create_poke("pikachu")]),
        Team.create_team(name="Stinky Stevies", members=[Pokemon.create_poke("grimer"), Pokemon.create_poke("trubbish")])]
    activePokemon : Pokemon = Pokemon.create_poke("shinx")
    activeTeam : Team = Team.create_team(name="Beefy Bois", members=[Pokemon.create_poke("snorlax")])

    @rx.var
    def show_active_pokemon(self) -> str:
        return self.activePokemon.pokemon_name
    
    def set_active_poke(self, name: str) -> None:
        self.activePokemon = Pokemon.create_poke(name=name)

    def set_active_team(self, name: str, members: List[Pokemon]) -> None:
        created_team = Team.create_team(name=name, members=members)
        self.activeTeam = created_team

    def cache_team(self, team: Team) -> None:
        if team not in self.teamsObj:
            self.teamsObj.append(team)
        else:
            print(f"{team.team_name} already exists.")
    
    def remove_team(self, team: Team) -> None: 
        if team in State.teamsObj: 
            State.teamsObj.remove(team) 
        else: print(f"ERROR: Team {team.team_name} not found.") 


#Components
componets = ["nav_bar", "display_pokemon", "display_team", "left_team_compare", "right_team_compare"]
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
            width="10rem",
        ),
    ),
    top="0px",
    padding="1em",
    height="4em",
    width="100%",
)

def poke_card(pokemon: Pokemon) -> rx.card:
    return rx.card(
        rx.heading(pokemon.pokemon_name)
    )

def poke_list(team: Team) -> rx.flex:
    return rx.flex(
        rx.foreach(team.members, poke_card)
    )

def team_card(team: Team) -> rx.card:
    return rx.card(
        rx.heading(team.team_name),
        poke_list(team=team)
    )

def team_list() -> rx.flex:
    return rx.flex(
        rx.foreach(State.teamsObj, team_card),
        direction="column"
    )

#Routes
#Home/Manage Teams
methods = ["nav", "create_team", "edit_team", "delete_team", "search?"]

def index() -> rx.Component:
    return rx.fragment(
        rx.vstack(
            nav_bar(),
            team_list(),
            rx.button(
                "Create Team", type="submit",
                on_click=State.cache_team(Team.create_team(name="Big Bois", members=[Pokemon.create_poke("snorlax")]))),
            spacing="5",
            min_height="85vh",
        ),
    )

#Team Detail View?
methods = ["nav", "add_teammates", "remove_teammates"]
def detail() -> rx.Component:
    return rx.fragment(
        nav_bar(),
        "Detail",
    )
#Team Comparison
methods = ["nav", "pick_teams", "edit_teams"]
def comparison() -> rx.Component:
    return rx.fragment(
        nav_bar(),
        "Compare",
    )

#About
def about() -> rx.Component:
    return rx.fragment(
        nav_bar(),
        "About",
    )


app = rx.App()
app.add_page(index, title="Home")
app.add_page(detail, title="Detail View")
app.add_page(comparison, title="Comparison View")
app.add_page(about, title="About")