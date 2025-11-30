from unittest import TestCase, main

from project.robot import Robot


class TestRobot(TestCase):
    def setUp(self):
        self.robot1 = Robot("John", "Education", 20, 100.0)
    
    def test_init(self):
        self.assertEqual("John", self.robot1.robot_id)
        self.assertEqual("Education", self.robot1.category)
        self.assertEqual(20, self.robot1.available_capacity)
        self.assertEqual(100.0, self.robot1.price)
        self.assertEqual([], self.robot1.hardware_upgrades)
        self.assertEqual([], self.robot1.software_updates)
    
    def test_set_category_raises(self):
        with self.assertRaises(ValueError) as e:
            self.robot1.category = "AAA"
        self.assertEqual("Category should be one of \'['Military', 'Education', 'Entertainment', 'Humanoids']\'",
                         str(e.exception))
    
    def test_set_price_raises(self):
        with self.assertRaises(ValueError) as e:
            self.robot1.price = -1
        self.assertEqual("Price cannot be negative!", str(e.exception))
    
    def test_upgrade_success(self):
        result = self.robot1.upgrade("HA", 20.0)
        self.assertEqual("Robot John was upgraded with HA.", result)
        self.assertEqual(["HA"], self.robot1.hardware_upgrades)
        self.assertEqual(130.0, self.robot1.price)
        
        result = self.robot1.upgrade("HB", 30.0)
        self.assertEqual("Robot John was upgraded with HB.", result)
        self.assertEqual(["HA", "HB"], self.robot1.hardware_upgrades)
        self.assertEqual(175.0, self.robot1.price)
    
    def test_upgrade_failed(self):
        result = self.robot1.upgrade("HA", 20.0)
        self.assertEqual("Robot John was upgraded with HA.", result)
        self.assertEqual(["HA"], self.robot1.hardware_upgrades)
        self.assertEqual(130.0, self.robot1.price)
        
        result = self.robot1.upgrade("HA", 30.0)
        self.assertEqual("Robot John was not upgraded.", result)
        self.assertEqual(["HA"], self.robot1.hardware_upgrades)
        self.assertEqual(130.0, self.robot1.price)
    
    def test_update_success_software_not_present(self):
        result = self.robot1.update(2.3, 5)
        self.assertEqual("Robot John was updated to version 2.3.", result)
        self.assertEqual([2.3], self.robot1.software_updates)
        self.assertEqual(15, self.robot1.available_capacity)
    
    def test_update_success_software_present(self):
        self.robot1.software_updates = [1.1, 1.4, 1.7, 2.0]
        result = self.robot1.update(2.3, 5)
        self.assertEqual("Robot John was updated to version 2.3.", result)
        self.assertEqual([1.1, 1.4, 1.7, 2.0, 2.3], self.robot1.software_updates)
        self.assertEqual(15, self.robot1.available_capacity)
    
    def test_update_failed_less_version_more_needed_capacity(self):
        self.robot1.software_updates = [1.1, 1.4, 1.7, 2.0]
        result = self.robot1.update(1.8, 25)
        self.assertEqual("Robot John was not updated.", result)
        self.assertEqual([1.1, 1.4, 1.7, 2.0], self.robot1.software_updates)
        self.assertEqual(20, self.robot1.available_capacity)
    
    def test_update_failed_max_version_more_needed_capacity(self):
        self.robot1.software_updates = [1.1, 1.4, 1.7, 2.0]
        result = self.robot1.update(2.0, 25)
        self.assertEqual("Robot John was not updated.", result)
        self.assertEqual([1.1, 1.4, 1.7, 2.0], self.robot1.software_updates)
        self.assertEqual(20, self.robot1.available_capacity)
    
    def test_update_failed_more_version_less_needed_capacity(self):
        self.robot1.software_updates = [1.1, 1.4, 1.7, 2.0]
        result = self.robot1.update(2.3, 25)
        self.assertEqual("Robot John was not updated.", result)
        self.assertEqual([1.1, 1.4, 1.7, 2.0], self.robot1.software_updates)
        self.assertEqual(20, self.robot1.available_capacity)
    
    def test_robot1_greater_than_robot2(self):
        robot2 = Robot("Anna", "Military", 30, 50)
        result = self.robot1 > robot2
        self.assertEqual("Robot with ID John is more expensive than Robot with ID Anna.", result)
    
    def test_robot1_lower_than_robot2(self):
        robot2 = Robot("Anna", "Military", 30, 150)
        result = self.robot1 > robot2
        self.assertEqual("Robot with ID John is cheaper than Robot with ID Anna.", result)
    
    def test_robot1_equal_to_robot2(self):
        robot2 = Robot("Anna", "Military", 30, 100)
        result = self.robot1 > robot2
        self.assertEqual("Robot with ID John costs equal to Robot with ID Anna.", result)


if __name__ == '__main__':
    main()
