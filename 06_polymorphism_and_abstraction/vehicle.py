from abc import ABC, abstractmethod


class Vehicle(ABC):
	def __init__(self, fuel_quantity: int, fuel_consumption: int):
		self.fuel_quantity = fuel_quantity
		self.fuel_consumption = fuel_consumption
	
	@abstractmethod
	def refuel(self, fuel: int):
		pass
	
	@abstractmethod
	def drive(self, distance: int):
		pass


class Car(Vehicle):
	AC_CONSUMPTION = 0.9
	
	def refuel(self, fuel: int):
		self.fuel_quantity += fuel
	
	def drive(self, distance: int):
		fuel_needed = (self.AC_CONSUMPTION + self.fuel_consumption) * distance
		if self.fuel_quantity >= fuel_needed:
			self.fuel_quantity -= fuel_needed


class Truck(Vehicle):
	AC_CONSUMPTION = 1.6
	
	def refuel(self, fuel: int):
		self.fuel_quantity += 0.95 * fuel
	
	def drive(self, distance: int):
		fuel_needed = (self.AC_CONSUMPTION + self.fuel_consumption) * distance
		if self.fuel_quantity >= fuel_needed:
			self.fuel_quantity -= fuel_needed


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
