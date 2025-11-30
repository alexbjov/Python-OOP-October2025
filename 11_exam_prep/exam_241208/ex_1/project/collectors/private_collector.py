from project.collectors.base_collector import BaseCollector


class PrivateCollector(BaseCollector):
    AVAILABLE_MONEY: float = 25_000.0
    INCREMENT_MONEY: float = 5_000.0
    AVAILABLE_SPACE: int = 3_000
    
    def __init__(self, name: str):
        super().__init__(name, self.AVAILABLE_MONEY, self.AVAILABLE_SPACE)
    
    def increase_money(self):
        self.available_money += self.INCREMENT_MONEY
