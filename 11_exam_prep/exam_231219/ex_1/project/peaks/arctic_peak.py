from project.peaks.base_peak import BasePeak


class ArcticPeak(BasePeak):
	GEAR = ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]
	
	def calculate_difficulty_level(self) -> str | None:
		if self.elevation > 3000:
			return "Extreme"
		elif 2000 <= self.elevation <= 3000:
			return "Advanced"
	
	def get_recommended_gear(self) -> list[str]:
		return self.GEAR
	
	@classmethod
	def from_arctic_peak(cls, name: str, elevation: int):
		return cls(name, elevation)
