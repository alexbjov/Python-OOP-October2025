from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
	def setUp(self):
		self.vehicle = Vehicle(50.0, 150.0)
	
	def test_init(self):
		self.assertEqual(50.0, self.vehicle.fuel)
		self.assertEqual(50.0, self.vehicle.capacity)
		self.assertEqual(150.0, self.vehicle.horse_power)
		self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)
	
	def test_drive_success(self):
		self.vehicle.drive(3)
		self.assertEqual(46.25, self.vehicle.fuel)
	
	def test_drive_error(self):
		with self.assertRaises(Exception) as ex:
			self.vehicle.drive(50)
		self.assertEqual('Not enough fuel', str(ex.exception))
	
	def test_refuel_success(self):
		self.vehicle.fuel = 25
		self.vehicle.refuel(5)
		self.assertEqual(30, self.vehicle.fuel)
	
	def test_refuel_error(self):
		with self.assertRaises(Exception) as ex:
			self.vehicle.refuel(2)
		self.assertEqual('Too much fuel', str(ex.exception))
	
	def test_str_method(self):
		res = f"The vehicle has 150.0 horse power with 50.0 fuel left and 1.25 fuel consumption"
		self.assertEqual(res, str(self.vehicle))


if __name__ == '__main__':
	main()
