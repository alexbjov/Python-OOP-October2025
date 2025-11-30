from project.collectors.base_collector import BaseCollector


class Museum(BaseCollector):
    AVAILABLE_MONEY: float = 15_000.0
    INCREMENT_MONEY: float = 1_000.0
    AVAILABLE_SPACE: int = 2_000
    
    def __init__(self, name: str):
        super().__init__(name, self.AVAILABLE_MONEY, self.AVAILABLE_SPACE)
    
    def increase_money(self):
        self.available_money += self.INCREMENT_MONEY
