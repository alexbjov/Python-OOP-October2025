from unittest import TestCase, main
from project.star_system import StarSystem


class TestStarSystem(TestCase):
    def setUp(self):
        self.star_system = StarSystem("A100", "Red giant", "Binary", 2)
    
    def test_init(self):
        self.assertEqual("A100", self.star_system.name)
        self.assertEqual("Red giant", self.star_system.star_type)
        self.assertEqual("Binary", self.star_system.system_type)
        self.assertEqual(2, self.star_system.num_planets)
        self.assertIsNone(self.star_system.habitable_zone_range)
        self.assertEqual(5, len(self.star_system._STAR_TYPES))
        self.assertEqual(4, len(self.star_system._STAR_SYSTEM_TYPES))
    
    
    def test_get_is_habitable_already_set_none(self):
        result = self.star_system.is_habitable
        self.assertFalse(result)
    
    def test_get_is_habitable_zero_planets(self):
        self.star_system.habitable_zone_range = (1, 3)
        self.star_system.num_planets = 0
        result = self.star_system.is_habitable
        self.assertFalse(result)
    
    def test_get_is_habitable_already_set_properly(self):
        self.star_system.habitable_zone_range = (1, 3)
        result = self.star_system.is_habitable
        self.assertTrue(result)
    
    def test_name(self):
        with self.assertRaises(ValueError) as ex:
            self.star_system.name = " "
        self.assertEqual("Name must be a non-empty string.", str(ex.exception))
        self.assertEqual("A100", self.star_system.name)
    
    def test_star_type(self):
        with self.assertRaises(ValueError) as ex:
            self.star_system.star_type = "Invalid star type"
        self.assertEqual("Star type must be one of ['Blue giant', 'Brown dwarf', 'Red dwarf', 'Red giant', 'Yellow dwarf'].", str(ex.exception))
        self.assertEqual("Red giant", self.star_system.star_type)
    
    def test_system_type(self):
        with self.assertRaises(ValueError) as ex:
            self.star_system.system_type = "Invalid system type"
        self.assertEqual("System type must be one of ['Binary', 'Multiple', 'Single', 'Triple'].", str(ex.exception))
        self.assertEqual("Binary", self.star_system.system_type)

    def test_num_planets(self):
        with self.assertRaises(ValueError) as ex:
            self.star_system.num_planets = -1
        self.assertEqual("Number of planets must be a non-negative integer.", str(ex.exception))
        self.assertEqual(2, self.star_system.num_planets)
    
    def test_habitable_zone_range_len_tuple_greater_than_two_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.star_system.habitable_zone_range = (1, 2, 3)
        
        self.assertEqual("Habitable zone range must be a tuple of two numbers (start, end) where start < end.",
                         str(ex.exception))
        self.assertIsNone(self.star_system.habitable_zone_range)
    
    def test_habitable_zone_range_len_tuple_two_equal_start_end_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.star_system.habitable_zone_range = (1, 1)
        
        self.assertEqual("Habitable zone range must be a tuple of two numbers (start, end) where start < end.",
                         str(ex.exception))
        self.assertIsNone(self.star_system.habitable_zone_range)
    
    def test_habitable_zone_range_len_tuple_two_start_greater_than_end_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.star_system.habitable_zone_range = (2, 1)
        
        self.assertEqual("Habitable zone range must be a tuple of two numbers (start, end) where start < end.",
                         str(ex.exception))
        self.assertIsNone(self.star_system.habitable_zone_range)

    def test_greater_than_success(self):
        self.star_system.habitable_zone_range = (1, 3)
        star_system_2 = StarSystem("B100", "Red dwarf", "Triple", 3)
        star_system_2.habitable_zone_range = (4, 5)

        result = self.star_system > star_system_2
        self.assertTrue(result)
    
    def test_greater_than_raises(self):
        self.star_system.habitable_zone_range = (1, 3)
        star_system_2 = StarSystem("B100", "Red dwarf", "Triple", 3)

        with self.assertRaises(ValueError) as ex:
            self.star_system > star_system_2
        self.assertTrue("Comparison not possible: One or both systems lack a defined habitable zone or planets.", str(ex.exception))
    
    def test_compare_star_systems_first_larger_than_second_success(self):
        self.star_system.habitable_zone_range = (1, 3)
        star_system_2 = StarSystem("B100", "Red dwarf", "Triple", 3)
        star_system_2.habitable_zone_range = (4, 5)
        
        result = StarSystem.compare_star_systems(self.star_system, star_system_2)
        self.assertEqual("A100 has a wider habitable zone than B100.", result)
    
    def test_compare_star_systems_first_less_than_second_success(self):
        self.star_system.habitable_zone_range = (1, 2)
        star_system_2 = StarSystem("B100", "Red dwarf", "Triple", 3)
        star_system_2.habitable_zone_range = (4, 6)
        
        result = StarSystem.compare_star_systems(self.star_system, star_system_2)
        self.assertEqual("B100 has a wider or equal habitable zone compared to A100.", result)

    def test_compare_star_systems(self):
        star_system_2 = [1, 2]
        result = StarSystem.compare_star_systems(self.star_system, star_system_2)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    main()
