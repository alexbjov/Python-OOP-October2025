from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    ALLOWED_PADS = {
        "KneePad": KneePad,
        "ElbowPad": ElbowPad
    }
    
    ALLOWED_TEAMS = {
        "IndoorTeam": IndoorTeam,
        "OutdoorTeam": OutdoorTeam
    }
    
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: list[BaseEquipment] = []
        self.teams: list[BaseTeam] = []
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value: str):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value
    
    def add_equipment(self, equipment_type: str) -> str:
        if equipment_type not in self.ALLOWED_PADS:
            raise Exception("Invalid equipment type!")
        
        new_equipment = self.ALLOWED_PADS[equipment_type]()
        self.equipment.append(new_equipment)
        return f"{equipment_type} was successfully added."
    
    def add_team(self, team_type: str, team_name: str, country: str, advantage: int) -> str:
        if team_type not in self.ALLOWED_TEAMS:
            raise Exception("Invalid team type!")
        
        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."
        
        new_team = self.ALLOWED_TEAMS[team_type](team_name, country, advantage)
        self.teams.append(new_team)
        return f"{team_type} was successfully added."
    
    def sell_equipment(self, equipment_type: str, team_name: str) -> str:
        searched_team = next((team for team in self.teams if team.name == team_name), None)
        
        position = -1
        for i in range(len(self.equipment) - 1, -1, -1):
            if self.equipment[i].__class__.__name__ == equipment_type:
                position = i
                break
        
        last_item = self.equipment[position]
        if searched_team.budget < last_item.price:
            raise Exception("Budget is not enough!")
        
        self.equipment.pop(position)
        searched_team.equipment.append(last_item)
        searched_team.budget -= last_item.price
        return f"Successfully sold {equipment_type} to {team_name}."
    
    def remove_team(self, team_name: str) -> str:
        searched_team = next((team for team in self.teams if team.name == team_name), None)
        if searched_team is None:
            raise Exception("No such team!")
        
        if searched_team.wins > 0:
            raise Exception(f"The team has {searched_team.wins} wins! Removal is impossible!")
        
        self.teams.remove(searched_team)
        return f"Successfully removed {team_name}."
    
    def increase_equipment_price(self, equipment_type: str) -> str:
        counter = 0
        for eq in self.equipment:
            if eq.__class__.__name__ == equipment_type:
                eq.increase_price()
                counter += 1
        
        return f"Successfully changed {counter}pcs of equipment."
    
    def play(self, team_name1: str, team_name2: str) -> str:
        searched_team_1 = [team1 for team1 in self.teams if team1.name == team_name1][0]
        searched_team_2 = [team2 for team2 in self.teams if team2.name == team_name2][0]
        if searched_team_1.__class__.__name__ != searched_team_2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")
        
        team_1_points = searched_team_1.advantage + sum(eq.protection for eq in searched_team_1.equipment)
        team_2_points = searched_team_2.advantage + sum(eq.protection for eq in searched_team_2.equipment)
        
        if team_1_points > team_2_points:
            searched_team_1.win()
            return f"The winner is {team_name1}."
        
        if team_1_points < team_2_points:
            searched_team_2.win()
            return f"The winner is {team_name2}."
        
        return "No winner in this game."
    
    def get_statistics(self) -> str:
        sorted_teams = sorted(self.teams, key=lambda team: -team.wins)
        output: list[str] = [
            f"Tournament: {self.name}",
            f"Number of Teams: {len(self.teams)}",
            "Teams:"
        ]
        
        for team in sorted_teams:
            output.append(team.get_statistics())
        
        return "\n".join(output)
