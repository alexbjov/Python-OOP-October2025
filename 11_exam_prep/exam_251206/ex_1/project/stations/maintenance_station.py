from project.astronauts.engineer_astronaut import EngineerAstronaut
from project.stations.base_station import BaseStation


class MaintenanceStation(BaseStation):
    SALARY_INCREASE: float = 3000.0
    
    def __init__(self, name: str):
        super().__init__(name, 3)
    
    def update_salaries(self, min_value: float) -> None:
        for a in self.astronauts:
            if isinstance(a, EngineerAstronaut) and a.salary <= min_value:
                a.salary += self.SALARY_INCREASE
