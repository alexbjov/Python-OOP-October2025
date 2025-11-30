from project.battleships.base_battleship import BaseBattleship


class PirateBattleship(BaseBattleship):
    AMMUNITION = 80
    AMMO_REDUCTION = 10
    
    def __init__(self, name: str, health: int, hit_strength: int):
        super().__init__(name, health, hit_strength, self.AMMUNITION)
    
    def attack(self) -> None:
        self.ammunition -= self.AMMO_REDUCTION
        if self.ammunition < 0:
            self.ammunition = 0
