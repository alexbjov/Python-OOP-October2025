from unittest import TestCase, main

from project.climbing_robot import ClimbingRobot


class TestClimbingRobot(TestCase):
	def setUp(self):
		self.robot = ClimbingRobot("Mountain", "A", 200, 100)
	
	def test_init(self):
		self.assertEqual('Mountain', self.robot.category)
		self.assertEqual("A", self.robot.part_type)
		self.assertEqual(200, self.robot.capacity)
		self.assertEqual(100, self.robot.memory)
		self.assertEqual([], self.robot.installed_software)
	
	def test_set_invalid_category(self):
		with self.assertRaises(ValueError) as e:
			self.robot.category = "A"
		self.assertEqual(
			"Category should be one of ['Mountain', 'Alpine', 'Indoor', 'Bouldering']",
			str(e.exception))
		self.assertEqual('Mountain', self.robot.category)
		self.assertEqual("A", self.robot.part_type)
		self.assertEqual(200, self.robot.capacity)
		self.assertEqual(100, self.robot.memory)
		self.assertEqual([], self.robot.installed_software)
	
	def test_set_valid_category(self):
		self.assertEqual("Mountain", self.robot.category)
		self.robot.category = "Alpine"
		self.assertEqual("Alpine", self.robot.category)
		self.assertEqual("A", self.robot.part_type)
		self.assertEqual(200, self.robot.capacity)
		self.assertEqual(100, self.robot.memory)
		self.assertEqual([], self.robot.installed_software)
	
	def test_get_used_capacity(self):
		result = self.robot.get_used_capacity()
		self.assertEqual(0, result)
		self.robot.install_software(
			{"name": "B", "capacity_consumption": 50, "memory_consumption": 50})
		result = self.robot.get_used_capacity()
		self.assertEqual(50, result)
		
		self.assertEqual('Mountain', self.robot.category)
		self.assertEqual("A", self.robot.part_type)
		self.assertEqual(150, self.robot.get_available_capacity())
		self.assertEqual(50, self.robot.get_available_memory())
		self.assertEqual([
			{"name": "B", "capacity_consumption": 50, "memory_consumption": 50}
		], self.robot.installed_software)
	
	def test_get_available_capacity(self):
		result = self.robot.get_available_capacity()
		self.assertEqual(200, result)
		self.robot.install_software(
			{"name": "B", "capacity_consumption": 50, "memory_consumption": 50})
		result = self.robot.get_available_capacity()
		self.assertEqual(150, result)
		
		self.assertEqual('Mountain', self.robot.category)
		self.assertEqual("A", self.robot.part_type)
		self.assertEqual(150, self.robot.get_available_capacity())
		self.assertEqual(50, self.robot.get_available_memory())
		self.assertEqual([
			{"name": "B", "capacity_consumption": 50, "memory_consumption": 50}
		], self.robot.installed_software)
	
	def test_get_used_memory(self):
		result = self.robot.get_used_memory()
		self.assertEqual(0, result)
		self.robot.install_software(
			{"name": "B", "capacity_consumption": 50, "memory_consumption": 50})
		result = self.robot.get_used_memory()
		self.assertEqual(50, result)
		
		self.assertEqual('Mountain', self.robot.category)
		self.assertEqual("A", self.robot.part_type)
		self.assertEqual(150, self.robot.get_available_capacity())
		self.assertEqual(50, self.robot.get_available_memory())
		self.assertEqual([
			{"name": "B", "capacity_consumption": 50, "memory_consumption": 50}
		], self.robot.installed_software)
	
	def test_get_available_memory(self):
		result = self.robot.get_available_memory()
		self.assertEqual(100, result)
		self.robot.install_software(
			{"name": "B", "capacity_consumption": 50, "memory_consumption": 50})
		result = self.robot.get_available_memory()
		self.assertEqual(50, result)
		
		self.assertEqual('Mountain', self.robot.category)
		self.assertEqual("A", self.robot.part_type)
		self.assertEqual(150, self.robot.get_available_capacity())
		self.assertEqual(50, self.robot.get_available_memory())
		self.assertEqual([
			{"name": "B", "capacity_consumption": 50, "memory_consumption": 50}
		], self.robot.installed_software)
	
	def test_install_software_success(self):
		result = self.robot.install_software(
			{"name": "B", "capacity_consumption": 200,
			 "memory_consumption": 100})
		self.assertEqual(
			"Software 'B' successfully installed on Mountain part.", result)
		
		self.assertEqual(0, self.robot.get_available_capacity())
		self.assertEqual(0, self.robot.get_available_memory())
		self.assertEqual([
			{"name": "B", "capacity_consumption": 200,
			 "memory_consumption": 100}
		], self.robot.installed_software)
	
	def test_install_software_more_capacity_failed(self):
		result = self.robot.install_software(
			{"name": "B", "capacity_consumption": 250,
			 "memory_consumption": 100})
		self.assertEqual("Software 'B' cannot be installed on Mountain part.",
			result)
		
		self.assertEqual(200, self.robot.get_available_capacity())
		self.assertEqual(100, self.robot.get_available_memory())
		self.assertEqual([], self.robot.installed_software)
	
	def test_install_software_more_memory_failed(self):
		result = self.robot.install_software(
			{"name": "B", "capacity_consumption": 200,
			 "memory_consumption": 150})
		self.assertEqual("Software 'B' cannot be installed on Mountain part.",
			result)
		
		self.assertEqual(200, self.robot.get_available_capacity())
		self.assertEqual(100, self.robot.get_available_memory())
		self.assertEqual([], self.robot.installed_software)
	
	def test_install_software_failed(self):
		result = self.robot.install_software(
			{"name": "B", "capacity_consumption": 250,
			 "memory_consumption": 150})
		self.assertEqual("Software 'B' cannot be installed on Mountain part.",
			result)
		
		self.assertEqual(200, self.robot.get_available_capacity())
		self.assertEqual(100, self.robot.get_available_memory())
		self.assertEqual([], self.robot.installed_software)


if __name__ == '__main__':
	main()
