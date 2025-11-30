from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    DELICACY_TYPES = {
        "Gingerbread": Gingerbread,
        "Stolen": Stolen
    }
    
    BOOTH_TYPES = {
        "Open Booth": OpenBooth,
        "Private Booth": PrivateBooth
    }
    
    def __init__(self):
        self.booths: list[Booth] = []
        self.delicacies: list[Delicacy] = []
        self.income: float = 0.0
    
    def add_delicacy(self, type_delicacy: str, name: str, price: float) -> str:
        searched_delicacy = next((delicacy for delicacy in self.delicacies if delicacy.name == name), None)
        if searched_delicacy:
            raise Exception(f"{name} already exists!")
        
        if type_delicacy not in self.DELICACY_TYPES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        
        new_delicacy = self.DELICACY_TYPES[type_delicacy](name, price)
        self.delicacies.append(new_delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."
    
    def add_booth(self, type_booth: str, booth_number: int, capacity: int) -> str:
        searched_booth = next((booth for booth in self.booths if booth.booth_number == booth_number), None)
        if searched_booth:
            raise Exception(f"Booth number {booth_number} already exists!")
        
        if type_booth not in self.BOOTH_TYPES:
            raise Exception(f"{type_booth} is not a valid booth!")
        
        new_booth = self.BOOTH_TYPES[type_booth](booth_number, capacity)
        self.booths.append(new_booth)
        return f"Added booth number {booth_number} in the pastry shop."
    
    def reserve_booth(self, number_of_people: int) -> str:
        searched_booth = next(
            (booth for booth in self.booths if not booth.is_reserved and booth.capacity >= number_of_people), None)
        if searched_booth is None:
            raise Exception(f"No available booth for {number_of_people} people!")
        
        searched_booth.reserve(number_of_people)
        return f"Booth {searched_booth.booth_number} has been reserved for {number_of_people} people."
    
    def order_delicacy(self, booth_number: int, delicacy_name: str) -> str:
        searched_booth = next((booth for booth in self.booths if booth.booth_number == booth_number), None)
        if searched_booth is None:
            raise Exception(f"Could not find booth {booth_number}!")
        
        searched_delicacy = next((delicacy for delicacy in self.delicacies if delicacy.name == delicacy_name), None)
        if searched_delicacy is None:
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        
        searched_booth.delicacy_orders.append(searched_delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."
    
    def leave_booth(self, booth_number: int) -> str:
        searched_booth = next((booth for booth in self.booths if booth.booth_number == booth_number), None)
        bill_to_pay = searched_booth.price_for_reservation + sum(
            delicacy.price for delicacy in searched_booth.delicacy_orders)
        self.income += bill_to_pay
        
        searched_booth.delicacy_orders.clear()
        searched_booth.price_for_reservation = 0.0
        searched_booth.is_reserved = False
        
        return f"Booth {booth_number}:\nBill: {bill_to_pay:.2f}lv."
    
    def get_income(self) -> str:
        return f"Income: {self.income:.2f}lv."
