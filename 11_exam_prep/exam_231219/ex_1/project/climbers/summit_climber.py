from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
	STRENGTH = 150
	
	def __init__(self, name: str):
		super().__init__(name, self.STRENGTH)
	
	def can_climb(self) -> bool:
		return self.strength >= 75
	
	def climb(self, peak: BasePeak) -> None:
		if peak.difficulty_level == "Advanced":
			self.strength -= 30 * 1.3
		elif peak.difficulty_level == "Extreme":
			self.strength -= 30 * 2.5
		
		self.conquered_peaks.append(peak.name)
	
	@classmethod
	def from_summit_climber(cls, name: str):
		return cls(name)
