from project.peaks.base_peak import BasePeak


class SummitPeak(BasePeak):
	GEAR = ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]
	
	def calculate_difficulty_level(self) -> str | None:
		if self.elevation > 2500:
			return "Extreme"
		elif 1500 <= self.elevation <= 2500:
			return "Advanced"
	
	def get_recommended_gear(self) -> list[str]:
		return self.GEAR
	
	@classmethod
	def from_summit_peak(cls, name: str, elevation: int):
		return cls(name, elevation)
