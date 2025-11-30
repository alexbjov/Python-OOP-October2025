from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    MAX_MILEAGE: float = 450.00
    
    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, self.MAX_MILEAGE)
    
    def drive(self, mileage: float) -> None:
        decrement = round(mileage / self.max_mileage * 100)
        self.battery_level -= decrement
