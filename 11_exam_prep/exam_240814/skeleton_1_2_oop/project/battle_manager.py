from project.battleships.base_battleship import BaseBattleship
from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone
from project.zones.pirate_zone import PirateZone
from project.zones.royal_zone import RoyalZone


class BattleManager:
    VALID_ZONES = {'RoyalZone': RoyalZone, 'PirateZone': PirateZone}
    VALID_SHIPS = {'RoyalBattleship': RoyalBattleship,
                   'PirateBattleship': PirateBattleship}
    
    def __init__(self):
        self.zones: list[BaseZone] = []
        self.ships: list[BaseBattleship] = []
    
    def add_zone(self, zone_type: str, zone_code: str) -> str:
        if zone_type not in self.VALID_ZONES:
            raise Exception('Invalid zone type!')
        
        searched_zone = [z for z in self.zones if z.code == zone_code]
        if searched_zone:
            raise Exception('Zone already exists!')
        
        new_zone = self.VALID_ZONES[zone_type](zone_code)
        self.zones.append(new_zone)
        return f'A zone of type {zone_type} was successfully added.'
    
    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int) -> str:
        if ship_type not in self.VALID_SHIPS:
            raise Exception(f'{ship_type} is an invalid type of ship!')
        
        new_ship = self.VALID_SHIPS[ship_type](name, health, hit_strength)
        self.ships.append(new_ship)
        return f'A new {ship_type} was successfully added.'
    
    @staticmethod
    def add_ship_to_zone(zone: BaseZone, ship: BaseBattleship) -> str:
        if zone.volume <= 0:
            return f'Zone {zone.code} does not allow more participants!'
        
        if ship.health <= 0:
            return f'Ship {ship.name} is considered sunk! Participation not allowed!'
        
        if not ship.is_available:
            return f'Ship {ship.name} is not available and could not participate!'
        
        if ((isinstance(ship, PirateBattleship) and isinstance(zone, PirateZone)) or
                (isinstance(ship, RoyalBattleship) and isinstance(zone, RoyalZone))):
            ship.is_attacking = True
        
        else:
            ship.is_attacking = False
        
        zone.ships.append(ship)
        ship.is_available = False
        zone.volume -= 1
        return f'Ship {ship.name} successfully participated in zone {zone.code}.'
    
    def remove_battleship(self, ship_name: str) -> str:
        searched_ship = [s for s in self.ships if s.name == ship_name]
        
        if len(searched_ship) == 0:
            return 'No ship with this name!'
        
        if not searched_ship[0].is_available:
            return 'The ship participates in zone battles! Removal is impossible!'
        
        self.ships.remove(searched_ship[0])
        return f'Successfully removed ship {ship_name}.'
    
    def start_battle(self, zone: BaseZone):
        own_ships = [s for s in zone.ships if s.is_attacking]
        enemy_ships = [s for s in zone.ships if not s.is_attacking]
        
        if not own_ships or not enemy_ships:
            return f'Not enough participants. The battle is canceled.'
        
        sorted_own_ships = sorted(own_ships, key=lambda s: -s.hit_strength)
        best_own_ship = sorted_own_ships[0]
        best_own_ship.attack()
        
        sorted_enemy_ships = sorted(enemy_ships, key=lambda s: -s.health)
        best_enemy_ship = sorted_enemy_ships[0]
        best_enemy_ship.take_damage(best_own_ship)
        
        if best_enemy_ship.health <= 0:
            zone.ships.remove(best_enemy_ship)
            self.ships.remove(best_enemy_ship)
            return f'{best_enemy_ship.name} lost the battle and was sunk.'
        
        if best_own_ship.ammunition <= 0:
            zone.ships.remove(best_own_ship)
            self.ships.remove(best_own_ship)
            return f"{best_own_ship.name} ran out of ammunition and leaves."
        
        return f'Both ships survived the battle.'
    
    def get_statistics(self) -> str:
        available_ships = [s.name for s in self.ships if s.is_available]
        result = [f"Available Battleships: {len(available_ships)}"]
        if available_ships:
            result.append(f"#{', '.join(available_ships)}#")
        result.append("***Zones Statistics:***")
        result.append(f"Total Zones: {len(self.zones)}")
        if self.zones:
            sorted_zones = sorted(self.zones, key=lambda zone: zone.code)
            for z in sorted_zones:
                result.append(z.zone_info())
        
        return '\n'.join(result)
