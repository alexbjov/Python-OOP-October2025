from project.teams.base_team import BaseTeam


class IndoorTeam(BaseTeam):
    BUDGET: float = 500.0
    ADVANTAGE_INCREASE: int = 145
    
    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, self.BUDGET)
    
    def win(self) -> None:
        self.advantage += self.ADVANTAGE_INCREASE
        self.wins += 1
