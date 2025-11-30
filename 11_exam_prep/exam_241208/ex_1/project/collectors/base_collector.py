from abc import ABC, abstractmethod

from project.artifacts.base_artifact import BaseArtifact


class BaseCollector(ABC):
    def __init__(self, name: str, available_money: float, available_space: int):
        self.name = name
        self.available_money = available_money
        self.available_space = available_space
        self.purchased_artifacts: list[BaseArtifact] = []
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value: str):
        if not value.strip().replace(' ', '').isalnum():
            raise ValueError("Collector name must contain letters, numbers, and optional white spaces between them!")
        self.__name = value
    
    @property
    def available_money(self):
        return self.__available_money
    
    @available_money.setter
    def available_money(self, value: float):
        if value < 0:
            raise ValueError("A collector cannot have a negative amount of money!")
        self.__available_money = value
    
    @property
    def available_space(self):
        return self.__available_space
    
    @available_space.setter
    def available_space(self, value: int):
        if value < 0:
            raise ValueError("A collector cannot have a negative space available for exhibitions!")
        self.__available_space = value
    
    def can_purchase(self, artifact_price: float, artifact_space_required: int) -> bool:
        if self.available_money >= artifact_price and self.available_space >= artifact_space_required:
            return True
        return False
    
    def __str__(self):
        if len(self.purchased_artifacts) == 0:
            return (f"Collector name: {self.name}; Money available: {self.available_money:.2f}; Space available: "
                    f"{self.available_space}; Artifacts: none")
        
        sorted_artifacts = sorted(self.purchased_artifacts, key=lambda artifact: artifact.name, reverse=True)
        result = (f"Collector name: {self.name}; Money available: {self.available_money:.2f}; Space available: "
                  f"{self.available_space}; Artifacts: ")
        
        output = []
        for artifact in sorted_artifacts:
            output.append(artifact.name)
        
        return result + ", ".join(output)
    
    @abstractmethod
    def increase_money(self):
        pass
