from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
	STRENGTH = 200
	
	def __init__(self, name: str):
		super().__init__(name, self.STRENGTH)
	
	def can_climb(self) -> bool:
		return self.strength >= 100
	
	def climb(self, peak: BasePeak) -> None:
		if peak.difficulty_level == "Extreme":
			self.strength -= 20 * 2
		elif peak.difficulty_level == "Advanced":
			self.strength *= 20 * 1.5
		
		self.conquered_peaks.append(peak.name)
	
	@classmethod
	def from_arctic_climber(cls, name: str):
		return cls(name)
