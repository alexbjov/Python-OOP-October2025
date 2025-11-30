from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    MAX_MILEAGE: float = 180.00
    ADDITIONAL_LOST_PERCENTAGE: int = 5
    
    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, self.MAX_MILEAGE)
    
    def drive(self, mileage: float) -> None:
        decrement = round(mileage / self.max_mileage * 100) + self.ADDITIONAL_LOST_PERCENTAGE
        self.battery_level -= decrement
