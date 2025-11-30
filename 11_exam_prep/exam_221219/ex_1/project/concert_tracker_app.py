from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIANS = {
        "Guitarist": Guitarist,
        "Drummer": Drummer,
        "Singer": Singer
    }
    
    VALID_CONCERT = {
        "Rock": {
            "Drummer": ["play the drums with drumsticks"],
            "Singer": ["sing high pitch notes"],
            "Guitarist": ["play rock"]
        },
        "Metal": {
            "Drummer": ["play the drums with drumsticks"],
            "Singer": ["sing low pitch notes"],
            "Guitarist": ["play metal"]
        },
        "Jazz": {
            "Drummer": ["play the drums with brushes"],
            "Singer": ["sing high pitch notes", "sing low pitch notes"],
            "Guitarist": ["play jazz"]
        }
    }
    
    def __init__(self):
        self.bands: list[Band] = []
        self.musicians: list[Musician] = []
        self.concerts: list[Concert] = []
    
    def create_musician(self, musician_type: str, name: str, age: int) -> str:
        if musician_type not in self.VALID_MUSICIANS:
            raise ValueError("Invalid musician type!")
        
        searched_musician = next((musician for musician in self.musicians if musician.name == name), None)
        if searched_musician:
            raise Exception(f"{name} is already a musician!")
        
        new_musician = self.VALID_MUSICIANS[musician_type](name, age)
        self.musicians.append(new_musician)
        return f"{name} is now a {musician_type}."
    
    def create_band(self, name: str) -> str:
        searched_band = next((band for band in self.bands if band.name == name), None)
        if searched_band:
            raise Exception(f"{name} band is already created!")
        
        new_band = Band(name)
        self.bands.append(new_band)
        return f"{name} was created."
    
    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str) -> str:
        searched_concert = next((concert for concert in self.concerts if concert.place == place), None)
        if searched_concert:
            raise Exception(f"{place} is already registered for {searched_concert.genre} concert!")
        
        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{genre} concert in {place} was added."
    
    def add_musician_to_band(self, musician_name: str, band_name: str) -> str:
        searched_musician = next((musician for musician in self.musicians if musician.name == musician_name), None)
        if searched_musician is None:
            raise Exception(f"{musician_name} isn't a musician!")
        
        searched_band = next((band for band in self.bands if band.name == band_name), None)
        if searched_band is None:
            raise Exception(f"{band_name} isn't a band!")
        
        searched_band.members.append(searched_musician)
        return f"{musician_name} was added to {band_name}."
    
    def remove_musician_from_band(self, musician_name: str, band_name: str) -> str:
        searched_band = next((band for band in self.bands if band.name == band_name), None)
        if searched_band is None:
            raise Exception(f"{band_name} isn't a band!")
        
        searched_musician = next((musician for musician in searched_band.members if musician.name == musician_name),
                                 None)
        if searched_musician is None:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        
        searched_band.members.remove(searched_musician)
        return f"{musician_name} was removed from {band_name}."
    
    def start_concert(self, concert_place: str, band_name: str) -> str:
        searched_band = [band for band in self.bands if band.name == band_name][0]
        if len(searched_band.members) < 3:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")
        else:
            musicians_set = {"Guitarist", "Drummer", "Singer"}
            for musician in searched_band.members:
                if musician.__class__.__name__ in musicians_set:
                    musicians_set.remove(musician.__class__.__name__)
                else:
                    break
            
            if musicians_set:
                raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")
        
        searched_concert = [concert for concert in self.concerts if concert.place == concert_place][0]
        concert_type = self.VALID_CONCERT[searched_concert.genre]  # {musician: [skills]}
        for musician in searched_band.members:
            for skill in concert_type[musician.__class__.__name__]:
                if skill not in musician.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
        
        profit = searched_concert.audience * searched_concert.ticket_price - searched_concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {searched_concert.genre} concert in {concert_place}."
