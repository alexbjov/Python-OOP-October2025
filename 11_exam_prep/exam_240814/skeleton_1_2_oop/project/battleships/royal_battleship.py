from project.battleships.base_battleship import BaseBattleship


class RoyalBattleship(BaseBattleship):
    AMMUNITION = 100
    AMMO_REDUCTION = 25
    
    def __init__(self, name: str, health: int, hit_strength: int):
        super().__init__(name, health, hit_strength, self.AMMUNITION)
    
    def attack(self) -> None:
        self.ammunition -= self.AMMO_REDUCTION
        if self.ammunition < 0:
            self.ammunition = 0
