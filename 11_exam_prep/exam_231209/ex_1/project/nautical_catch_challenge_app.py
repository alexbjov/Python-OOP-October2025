from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    ALLOWED_DIVERS = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    ALLOWED_FISH = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}
    
    def __init__(self):
        self.divers: list[BaseDiver] = []
        self.fish_list: list[BaseFish] = []
    
    def dive_into_competition(self, diver_type: str, diver_name: str) -> str:
        if diver_type not in self.ALLOWED_DIVERS:
            return f"{diver_type} is not allowed in our competition."
        
        searched_diver = next((d for d in self.divers if d.name == diver_name),
                              None)
        if searched_diver:
            return f"{diver_name} is already a participant."
        
        new_diver = self.ALLOWED_DIVERS[diver_type](diver_name)
        self.divers.append(new_diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."
    
    def swim_into_competition(self, fish_type: str, fish_name: str,
                              points: float) -> str:
        if fish_type not in self.ALLOWED_FISH:
            return f"{fish_type} is forbidden for chasing in our competition."
        
        searched_fish = next((f for f in self.fish_list if f.name == fish_name),
                             None)
        if searched_fish:
            return f"{fish_name} is already permitted."
        
        new_fish = self.ALLOWED_FISH[fish_type](fish_name, points)
        self.fish_list.append(new_fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."
    
    def chase_fish(self, diver_name: str, fish_name: str,
                   is_lucky: bool) -> str:
        searched_diver = next((d for d in self.divers if d.name == diver_name),
                              None)
        
        if not searched_diver:
            return f"{diver_name} is not registered for the competition."
        
        searched_fish = next((f for f in self.fish_list if f.name == fish_name),
                             None)
        
        if not searched_fish:
            return f"The {fish_name} is not allowed to be caught in this competition."
        
        if searched_diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."
        
        if searched_diver.oxygen_level < searched_fish.time_to_catch:
            searched_diver.miss(searched_fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."
        
        if searched_diver.oxygen_level == searched_fish.time_to_catch:
            if is_lucky:
                searched_diver.hit(searched_fish)
                return f"{diver_name} hits a {searched_fish.points:.1f}pt. {fish_name}."
            
            searched_diver.miss(searched_fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."
        
        searched_diver.hit(searched_fish)
        return f"{diver_name} hits a {searched_fish.points}pt. {fish_name}."
    
    def health_recovery(self) -> str:
        counter = 0
        for diver in self.divers:
            if diver.has_health_issue:
                diver.update_health_status()
                diver.renew_oxy()
                counter += 1
        
        return f"Divers recovered: {counter}"
    
    def diver_catch_report(self, diver_name: str) -> str:
        searched_diver = next((d for d in self.divers if d.name == diver_name),
                              None)
        output: list[str] = [
            f"**{diver_name} Catch Report**"
        ]
        for fish in searched_diver.catch:
            output.append(fish.fish_details())
        
        return "\n".join(output)
    
    def competition_statistics(self) -> str:
        output: list[str] = ["**Nautical Catch Challenge Statistics**"]
        healthy_divers = [d for d in self.divers if not d.has_health_issue]
        healthy_divers.sort(
            key=lambda x: (-x.competition_points, -len(x.catch), x.name))
        
        for diver in healthy_divers:
            output.append(str(diver))
        
        return "\n".join(output)
