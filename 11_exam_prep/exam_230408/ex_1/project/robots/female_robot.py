from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    WEIGHT: int = 7
    WEIGHT_INCREMENT: int = 1
    POSSIBLE_SERVICE = "SecondaryService"
    
    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, self.WEIGHT)
    
    def eating(self) -> None:
        self.weight += self.WEIGHT_INCREMENT
