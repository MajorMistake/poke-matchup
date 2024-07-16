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
        r = requests.get(
            f"https://pokeapi.co/api/v2/pokemon/{name}"
            )
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

        created_pokemon = Pokemon(
            pokemon_name=pokemon["name"], types=pokemon["types"],
            stats=pokemon["stats"], abilities=pokemon["abilities"],
            moves=pokemon["moves"])

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