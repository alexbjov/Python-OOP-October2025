from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.passenger_car import PassengerCar

from project.vehicles.cargo_van import CargoVan


class ManagingApp:
    ALLOWED_VEHICLES = {
        "PassengerCar": PassengerCar,
        "CargoVan": CargoVan
    }
    
    def __init__(self):
        self.users: list[User] = []
        self.vehicles: list[BaseVehicle] = []
        self.routes: list[Route] = []
    
    def register_user(self, first_name: str, last_name: str, driving_license_number: str) -> str:
        searched_driver = next(
            (driver for driver in self.users if driver.driving_license_number == driving_license_number), None)
        
        if searched_driver:
            return f"{driving_license_number} has already been registered to our platform."
        
        new_driver = User(first_name, last_name, driving_license_number)
        self.users.append(new_driver)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"
    
    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str) -> str:
        if vehicle_type not in self.ALLOWED_VEHICLES:
            return f"Vehicle type {vehicle_type} is inaccessible."
        
        searched_vehicle = next(
            (vehicle for vehicle in self.vehicles if vehicle.license_plate_number == license_plate_number), None)
        if searched_vehicle:
            return f"{license_plate_number} belongs to another vehicle."
        
        new_vehicle = self.ALLOWED_VEHICLES[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(new_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."
    
    def allow_route(self, start_point: str, end_point: str, length: float) -> str:
        searched_route = next(
            (route for route in self.routes if
             route.start_point == start_point and route.end_point == end_point and route.length == length), None)
        
        if searched_route:
            return f"{start_point}/{end_point} - {length} km had already been added to our platform."
        
        searched_route = next(
            (route for route in self.routes if
             route.start_point == start_point and route.end_point == end_point and route.length < length), None)
        
        if searched_route:
            return f"{start_point}/{end_point} shorter route had already been added to our platform."
        
        searched_route = next(
            (route for route in self.routes if
             route.start_point == start_point and route.end_point == end_point and route.length > length), None)
        
        if searched_route:
            searched_route.is_locked = True
        
        route_id = len(self.routes) + 1
        new_route = Route(start_point, end_point, length, route_id)
        self.routes.append(new_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."
    
    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool) -> str:
        searched_driver = next(
            (driver for driver in self.users if driver.driving_license_number == driving_license_number), None)
        searched_vehicle = next(
            (vehicle for vehicle in self.vehicles if vehicle.license_plate_number == license_plate_number), None)
        searched_route = next((route for route in self.routes if route.route_id == route_id), None)
        
        if searched_driver.is_blocked:
            searched_route.is_locked = True
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        
        if searched_vehicle.is_damaged:
            searched_route.is_locked = True
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        
        if searched_route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."
        
        searched_vehicle.drive(searched_route.length)
        
        if is_accident_happened:
            searched_vehicle.is_damaged = True
            searched_driver.decrease_rating()
        else:
            searched_driver.increase_rating()
        
        return (f"{searched_vehicle.brand} {searched_vehicle.model} License plate: "
                f"{searched_vehicle.license_plate_number} Battery: {searched_vehicle.battery_level}% "
                f"Status: {'Damaged' if searched_vehicle.is_damaged else 'OK'}")
    
    def repair_vehicles(self, count: int) -> str:
        start_counter = 0
        damaged_vehicles: list[BaseVehicle] = []
        for vehicle in self.vehicles:
            if vehicle.is_damaged:
                damaged_vehicles.append(vehicle)
        
        sorted_vehicles: list[BaseVehicle] = sorted(damaged_vehicles, key=lambda x: (x.brand, x.model))
        for vehicle in sorted_vehicles:
            if start_counter == count:
                break
            
            # idx = self.vehicles.index(vehicle)
            # self.vehicles[idx].change_status()
            # self.vehicles[idx].recharge()
            
            vehicle.change_status()
            vehicle.recharge()
            start_counter += 1
        
        return f"{start_counter} vehicles were successfully repaired!"
    
    def users_report(self) -> str:
        sorted_drivers = sorted(self.users, key=lambda x: -x.rating)
        output: list[str] = ["*** E-Drive-Rent ***"]
        for driver in sorted_drivers:
            output.append(str(driver))
        
        return "\n".join(output)
