from project.animals.animal import Bird
from project.food import Fruit, Meat, Vegetable, Seed, Food


class Owl(Bird):
    @property
    def weight_increment(self) -> float:
        return 0.25
    
    @property
    def allowed_food(self) -> list[Food]:
        return [Meat]
    
    @staticmethod
    def make_sound() -> str:
        return "Hoot Hoot"


class Hen(Bird):
    @property
    def weight_increment(self) -> float:
        return 0.35
    
    @property
    def allowed_food(self) -> list[Food]:
        return [Fruit, Meat, Vegetable, Seed]
    
    @staticmethod
    def make_sound() -> str:
        return "Cluck"
