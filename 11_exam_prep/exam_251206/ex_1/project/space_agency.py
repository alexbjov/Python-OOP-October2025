from project.astronauts.base_astronaut import BaseAstronaut
from project.astronauts.engineer_astronaut import EngineerAstronaut
from project.astronauts.scientist_astronaut import ScientistAstronaut
from project.stations.base_station import BaseStation
from project.stations.maintenance_station import MaintenanceStation
from project.stations.research_station import ResearchStation


class SpaceAgency:
    ASTRONAUT_TYPES = {
        "EngineerAstronaut": EngineerAstronaut,
        "ScientistAstronaut": ScientistAstronaut
    }
    
    STATION_TYPES = {
        "MaintenanceStation": MaintenanceStation,
        "ResearchStation": ResearchStation
    }
    
    def __init__(self):
        self.astronauts: list[BaseAstronaut] = []
        self.stations: list[BaseStation] = []
    
    def add_astronaut(self, astronaut_type: str, astronaut_id_number: str, astronaut_salary: float):
        if astronaut_type not in self.ASTRONAUT_TYPES:
            raise ValueError("Invalid astronaut type!")
        
        searched_astronaut = next((a for a in self.astronauts if a.id_number == astronaut_id_number), None)
        if searched_astronaut:
            raise ValueError(f"{astronaut_id_number} has been already added!")
        
        new_astronaut = self.ASTRONAUT_TYPES[astronaut_type](astronaut_id_number, astronaut_salary)
        self.astronauts.append(new_astronaut)
        return f"{astronaut_id_number} is successfully hired as {astronaut_type}."
    
    def add_station(self, station_type: str, station_name: str):
        if station_type not in self.STATION_TYPES:
            raise ValueError("Invalid station type!")
        
        searched_station = next((s for s in self.stations if s.name == station_name), None)
        if searched_station:
            raise ValueError(f"{station_name} has been already added!")
        
        new_station = self.STATION_TYPES[station_type](station_name)
        self.stations.append(new_station)
        return f"{station_name} is successfully added as a {station_type}."
    
    def assign_astronaut(self, station_name: str, astronaut_type: str):
        searched_station = next((s for s in self.stations if s.name == station_name), None)
        if searched_station is None:
            raise ValueError(f"Station {station_name} does not exist!")
        
        searched_astronaut = next((a for a in self.astronauts if a.__class__.__name__ == astronaut_type), None)
        if searched_astronaut is None:
            raise ValueError("No available astronauts of the type!")
        
        if searched_station.capacity <= len(searched_station.astronauts):
            return "This station has no available capacity."
        
        self.astronauts.remove(searched_astronaut)
        searched_station.astronauts.append(searched_astronaut)
        
        return f"{searched_astronaut.id_number} was assigned to {searched_station.name}."

    def train_astronauts(self, station: BaseStation, sessions_number: int):
        for _ in range(sessions_number):
            for a in station.astronauts:
                a.train()
        
        total_stamina = sum(a.stamina for a in station.astronauts)
        return f"{station.name} astronauts have {total_stamina} total stamina after {sessions_number} training session/s."
    
    def retire_astronaut(self, station: BaseStation, astronaut_id_number: str):
        searched_astronaut = next((a for a in station.astronauts if a.id_number == astronaut_id_number), None)
        if searched_astronaut is None or searched_astronaut.stamina == 100:
            return "The retirement process was canceled."
        
        station.astronauts.remove(searched_astronaut)
        # self.astronauts.append(searched_astronaut)
        return f"Retired astronaut {astronaut_id_number}."
    
    def agency_update(self, min_value: float):
        for station in self.stations:
            station.update_salaries(min_value)
        
        sorted_stations = sorted(self.stations, key=lambda s: (-len(s.astronauts), s.name))
        
        result = [
            "*Space Agency Up-to-Date Report*",
            f"Total number of available astronauts: {len(self.astronauts)}",
            f"**Stations count: {len(self.stations)}; Total available capacity: {sum(s.available_capacity for s in sorted_stations)}**"
        ]
        for station in sorted_stations:
            result.append(station.status())

        return "\n".join(result)
