from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    ALLOWED_TYPES = {
        "Desktop Computer": DesktopComputer,
        "Laptop": Laptop
    }
    
    def __init__(self):
        self.warehouse: list[Computer] = []
        self.profits: int = 0
    
    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int) -> str:
        if type_computer not in self.ALLOWED_TYPES:
            raise ValueError(f"{type_computer} is not a valid type computer!")
        
        new_computer = self.ALLOWED_TYPES[type_computer](manufacturer, model)
        result = new_computer.configure_computer(processor, ram)
        self.warehouse.append(new_computer)
        return result
    
    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int) -> str:
        searched_computer = next(
            (c for c in self.warehouse if
             c.price <= client_budget and wanted_processor == c.processor and c.ram >= wanted_ram), None)
        
        if searched_computer is None:
            raise Exception(f"Sorry, we don't have a computer for you.")
        
        self.warehouse.remove(searched_computer)
        self.profits += client_budget - searched_computer.price
        return repr(searched_computer) + f" sold for {client_budget}$."
