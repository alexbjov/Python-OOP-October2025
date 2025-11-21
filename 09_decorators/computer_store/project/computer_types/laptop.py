from project.computer_types.computer import Computer


class Laptop(Computer):
    TYPE = "laptop"
    MAX_RAM = 64
    
    PROCESSORS = {
        "AMD Ryzen 9 5950X": 900,
        "Intel Core i9-11900H": 1050,
        "Apple M1 Pro": 1200
    }
    
    @property
    def available_processors(self) -> dict[str, int]:
        return self.PROCESSORS
    
    @property
    def max_ram(self) -> int:
        return self.MAX_RAM
    
    def __str__(self):
        return self.TYPE
