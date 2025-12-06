import string
from abc import ABC, abstractmethod

from project.astronauts.base_astronaut import BaseAstronaut


class BaseStation(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.astronauts: list[BaseAstronaut] = []
    
    @property
    def available_capacity(self):
        return self.capacity - len(self.astronauts)
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value: str):
        for ch in value:
            criterion_1 = ch in string.ascii_letters
            criterion_2 = ch in string.digits
            criterion_3 = ch == '-'
            if not (criterion_1 or criterion_2 or criterion_3):
                raise ValueError("Station names can contain only letters, numbers, and hyphens!")
        self.__name = value
    
    @property
    def capacity(self):
        return self.__capacity
    
    @capacity.setter
    def capacity(self, value: int):
        if value < 0:
            raise ValueError("A station cannot have a negative capacity!")
        self.__capacity = value
    
    def calculate_total_salaries(self) -> str:
        total_salaries = 0
        if len(self.astronauts) > 0:
            total_salaries = sum(a.salary for a in self.astronauts)
        return f"{total_salaries:.2f}"
    
    def status(self) -> str:
        astronauts_str: list[str] = []
        if not self.astronauts:
            astronauts_str.append("N/A")
        else:
            sorted_astronauts = sorted(self.astronauts, key=lambda astronaut: astronaut.id_number)
            for a in sorted_astronauts:
                astronauts_str.append(a.id_number)
        
        return f"Station name: {self.name}; Astronauts: {' #'.join(astronauts_str)}; Total salaries: {self.calculate_total_salaries()}"

    @abstractmethod
    def update_salaries(self, min_value: float) -> None:
        pass