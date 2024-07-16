import reflex as rx

from typing import List

from .schema import Team, Pokemon


class State(rx.State):
    teamsObj : List[Team] = [
        Team.create_team(
            name="Team Titans",
            members=[Pokemon.create_poke("pikachu")]
            ),
        Team.create_team(
            name="Stinky Stevies",
            members=[Pokemon.create_poke("grimer"),
                     Pokemon.create_poke("trubbish")]
                     )]
    activePokemon : List[Pokemon] = []
    activeTeam : Team | None = None

    def set_active_poke(self, name: str) -> None:
        self.activePokemon.append(
            Pokemon.create_poke(name=name)
            )

    def set_active_team(self, name: str, members: List[Pokemon]) -> None:
        created_team = Team.create_team(
            name=name, members=members
            )
        self.activeTeam = created_team

    def save_team(self, team: Team) -> None:
        if team not in self.teamsObj:
            self.teamsObj.append(team)
        else:
            print(f"{team.team_name} already exists.")
    
    def remove_team(self, team: Team) -> None: 
        if team in State.teamsObj: 
            State.teamsObj.remove(team) 
        else: print(f"ERROR: Team {team.team_name} not found.") 