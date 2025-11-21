from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    TYPE = "desktop computer"
    MAX_RAM = 128
    
    PROCESSORS = {
        "AMD Ryzen 7 5700G": 500,
        "Intel Core i5-12600K": 600,
        "Apple M1 Max": 1800
    }
    
    @property
    def available_processors(self) -> dict[str, int]:
        return self.PROCESSORS
    
    @property
    def max_ram(self) -> int:
        return self.MAX_RAM
    
    def __str__(self):
        return self.TYPE
