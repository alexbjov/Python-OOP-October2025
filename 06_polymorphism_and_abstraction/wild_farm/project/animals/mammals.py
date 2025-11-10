from project.animals.animal import Mammal
from project.food import Fruit, Meat, Vegetable, Food


class Mouse(Mammal):
    @property
    def weight_increment(self) -> float:
        return 0.1
    
    @property
    def allowed_food(self) -> list[Food]:
        return [Vegetable, Fruit]
    
    @staticmethod
    def make_sound() -> str:
        return "Squeak"


class Dog(Mammal):
    @property
    def weight_increment(self) -> float:
        return 0.4
    
    @property
    def allowed_food(self) -> list[Food]:
        return [Meat]
    
    @staticmethod
    def make_sound() -> str:
        return "Woof!"


class Cat(Mammal):
    @property
    def weight_increment(self) -> float:
        return 0.3
    
    @property
    def allowed_food(self) -> list[Food]:
        return [Vegetable, Meat]
    
    @staticmethod
    def make_sound() -> str:
        return "Meow"


class Tiger(Mammal):
    @property
    def weight_increment(self) -> float:
        return 1.0
    
    @property
    def allowed_food(self) -> list[Food]:
        return [Meat]
    
    @staticmethod
    def make_sound() -> str:
        return "ROAR!!!"
