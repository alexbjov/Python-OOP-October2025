from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    DEFAULT_OXYGEN_LEVEL = 120
    
    def __init__(self, name: str):
        super().__init__(name, self.DEFAULT_OXYGEN_LEVEL)
    
    def renew_oxy(self) -> None:
        self.oxygen_level = self.DEFAULT_OXYGEN_LEVEL
    
    def miss(self, time_to_catch: int) -> None:
        if self.oxygen_level >= 0.6 * time_to_catch:
            self.oxygen_level -= 0.6 * time_to_catch
            self.oxygen_level = round(self.oxygen_level)
        else:
            self.oxygen_level = 0
        
        if self.oxygen_level == 0:
            self.has_health_issue = True
