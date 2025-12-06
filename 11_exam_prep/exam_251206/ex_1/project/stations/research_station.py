from project.astronauts.scientist_astronaut import ScientistAstronaut
from project.stations.base_station import BaseStation


class ResearchStation(BaseStation):
    SALARY_INCREASE: float = 5000.0
    
    def __init__(self, name: str):
        super().__init__(name, 5)
    
    def update_salaries(self, min_value: float) -> None:
        for a in self.astronauts:
            if isinstance(a, ScientistAstronaut) and a.salary <= min_value:
                a.salary += self.SALARY_INCREASE
