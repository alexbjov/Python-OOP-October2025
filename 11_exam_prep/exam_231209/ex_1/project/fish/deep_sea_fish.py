from project.fish.base_fish import BaseFish


class DeepSeaFish(BaseFish):
	def __init__(self, name: str, points: float):
		super().__init__(name, points, 180)
	
	def fish_details(self) -> str:
		return f"{self.__class__.__name__}: {self.name} [Points: {self.points:.1f}, Time to Catch: {self.time_to_catch} seconds]"
