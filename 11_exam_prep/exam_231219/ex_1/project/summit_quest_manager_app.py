from project.climbers.arctic_climber import ArcticClimber
from project.climbers.base_climber import BaseClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.base_peak import BasePeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
	CLIMBER_TYPES = ["ArcticClimber", "SummitClimber"]
	PEAK_TYPES = ["ArcticPeak", "SummitPeak"]
	
	def __init__(self):
		self.climbers: list[BaseClimber] = []
		self.peaks: list[BasePeak] = []
	
	def register_climber(self, climber_type: str, climber_name: str) -> str:
		if climber_type not in self.CLIMBER_TYPES:
			return f"{climber_type} doesn't exist in our register."
		
		searched_climber = next(
			(c for c in self.climbers if c.name == climber_name), None)
		if searched_climber:
			return f"{climber_name} has been already registered."
		
		new_climber = None
		if climber_type == "ArcticClimber":
			new_climber = ArcticClimber.from_arctic_climber(climber_name)
		elif climber_type == "SummitClimber":
			new_climber = SummitClimber.from_summit_climber(climber_name)
		
		self.climbers.append(new_climber)
		return f"{climber_name} is successfully registered as a {climber_type}."
	
	def peak_wish_list(self, peak_type: str, peak_name: str,
			peak_elevation: int) -> str:
		if peak_type not in self.PEAK_TYPES:
			return f"{peak_type} is an unknown type of peak."
		
		peak = None
		if peak_type == "ArcticPeak":
			peak = ArcticPeak.from_arctic_peak(peak_name, peak_elevation)
		elif peak_type == "SummitPeak":
			peak = SummitPeak.from_summit_peak(peak_name, peak_elevation)
		
		self.peaks.append(peak)
		return f"{peak_name} is successfully added to the wish list as a {peak_type}."
	
	def check_gear(self, climber_name: str, peak_name: str,
			gear: list[str]) -> str:
		searched_peak = next((p for p in self.peaks if p.name == peak_name),
			None)
		searched_climber = next(
			(c for c in self.climbers if c.name == climber_name), None)
		
		missing_gear = set(searched_peak.get_recommended_gear()) - set(gear)
		
		if missing_gear:
			sorted_missing_gear = sorted(missing_gear)
			searched_climber.is_prepared = False
			return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(sorted_missing_gear)}."
		
		searched_climber.is_prepared = True
		return f"{climber_name} is prepared to climb {peak_name}."
	
	def perform_climbing(self, climber_name: str, peak_name: str) -> str:
		searched_climber = next(
			(c for c in self.climbers if c.name == climber_name), None)
		if not searched_climber:
			return f"Climber {climber_name} is not registered yet."
		
		searched_peak = next((p for p in self.peaks if p.name == peak_name),
			None)
		if not searched_peak:
			return f"Peak {peak_name} is not part of the wish list."
		
		if searched_climber.is_prepared and searched_climber.can_climb():
			searched_climber.climb(searched_peak)
			return f"{climber_name} conquered {peak_name} whose difficulty level is {searched_peak.difficulty_level}."
		
		elif not searched_climber.is_prepared:
			return f"{climber_name} will need to be better prepared next time."
		
		searched_climber.rest()
		return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."
	
	def get_statistics(self) -> str:
		successful_climbers = [c for c in self.climbers if c.conquered_peaks]
		sorted_climbers = sorted(successful_climbers,
			key=lambda x: (-len(x.conquered_peaks), x.name))
		
		output: list[str] = [
			f"Total climbed peaks: {len(self.peaks)}",
			"**Climber's statistics:**"
		]
		for c in sorted_climbers:
			output.append(str(c))
		
		return "\n".join(output)
