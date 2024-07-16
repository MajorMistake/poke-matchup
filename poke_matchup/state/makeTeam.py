import requests
import json

from typing import List

from .baseState import State


class MakeTeam(State):
    openDialog: bool = False
    autocomplete_pokemon: List[str] = []
    pokeInput: str = ""

    def possible_pokemon(self) -> None:
        # To-Do Make Limit Dynamic/Try Implementing a Search
        # Via API
        r = requests.get(
            f"https://pokeapi.co/api/v2/pokemon?limit=10000"
            )
        data = json.loads(r.text)
        possible_names = [
            pokemon["name"] for pokemon in data["results"]
            ]
        self.autocomplete_pokemon = [
            name for name in possible_names
            if str(self.pokeInput) in name.lower()
            ]
        
    def toggleDialog(self) -> None:
        self.openDialog = not self.openDialog