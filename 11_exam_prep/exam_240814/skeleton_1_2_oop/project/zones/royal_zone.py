from project.battleships.pirate_battleship import PirateBattleship
from project.zones.base_zone import BaseZone


class RoyalZone(BaseZone):
    VOLUME = 10
    
    def __init__(self, code: str):
        super().__init__(code, self.VOLUME)
    
    def zone_info(self) -> str:
        pirate_ships_count = len(
            [s for s in self.ships if isinstance(s, PirateBattleship)])
        output = [
            f'@Royal Zone Statistics@',
            f'Code: {self.code}; Volume: {self.volume}',
            f"Battleships currently in the Royal Zone: {len(self.ships)}, "
            f"{pirate_ships_count} out of them are Pirate Battleships."
        ]
        if self.ships:
            ships_names = ', '.join([s.name for s in self.get_ships()])
            output.append(f"#{ships_names}#")
        
        return '\n'.join(output)
