from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    WEIGHT: int = 9
    WEIGHT_INCREMENT: int = 3
    POSSIBLE_SERVICE = "MainService"
    
    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, self.WEIGHT)
    
    def eating(self) -> None:
        self.weight += self.WEIGHT_INCREMENT
