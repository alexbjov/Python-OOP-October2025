from unittest import TestCase, main

from project.furniture import Furniture


class TestFurniture(TestCase):
    def setUp(self):
        self.item = Furniture("A", 5.0, (1, 2, 3), False, 3.0)
    
    def test_init_with_all_params(self):
        self.assertEqual("A", self.item.model)
        self.assertEqual(5.0, self.item.price)
        self.assertEqual((1, 2, 3), self.item.dimensions)
        self.assertFalse(self.item.in_stock)
        self.assertEqual(3.0, self.item.weight)
    
    def test_init_with_default_params(self):
        self.item.in_stock = True
        self.item.weight = None
        self.assertEqual("A", self.item.model)
        self.assertEqual(5.0, self.item.price)
        self.assertEqual((1, 2, 3), self.item.dimensions)
        self.assertTrue(self.item.in_stock)
        self.assertIsNone(self.item.weight)
    
    def test_set_model_error(self):
        with self.assertRaises(ValueError) as e:
            self.item.model = ''
        self.assertEqual(
            "Model must be a non-empty string with a maximum length of 50 characters.",
            str(e.exception))
        
        self.assertEqual('A', self.item.model)
        
        with self.assertRaises(ValueError) as e:
            self.item.model = 'A' * 51
        self.assertEqual(
            "Model must be a non-empty string with a maximum length of 50 characters.",
            str(e.exception))
        self.assertEqual('A', self.item.model)
    
    def test_set_model(self):
        self.assertEqual('A', self.item.model)
        self.item.model = 'B'
        self.assertEqual('B', self.item.model)
    
    def test_negative_price_error(self):
        with self.assertRaises(ValueError) as e:
            self.item.price = -1.0
        
        self.assertEqual("Price must be a non-negative number.",
                         str(e.exception))
        self.assertEqual(5.0, self.item.price)
    
    def test_invalid_length_dimensions_error(self):
        with self.assertRaises(ValueError) as e:
            self.item.dimensions = (1, 2)
        
        self.assertEqual("Dimensions tuple must contain 3 integers.",
                         str(e.exception))
        self.assertEqual((1, 2, 3), self.item.dimensions)
        
        with self.assertRaises(ValueError) as e:
            self.item.dimensions = (1, 2, 3, 4)
        
        self.assertEqual("Dimensions tuple must contain 3 integers.",
                         str(e.exception))
        self.assertEqual((1, 2, 3), self.item.dimensions)
    
    def test_negative_dimension_error(self):
        with self.assertRaises(ValueError) as e:
            self.item.dimensions = (-1, 2, 3)
        
        self.assertEqual(
            "Dimensions tuple must contain integers greater than zero.",
            str(e.exception))
        self.assertEqual((1, 2, 3), self.item.dimensions)
        
        with self.assertRaises(ValueError) as e:
            self.item.dimensions = (1, -2, 3)
        
        self.assertEqual(
            "Dimensions tuple must contain integers greater than zero.",
            str(e.exception))
        self.assertEqual((1, 2, 3), self.item.dimensions)
        
        with self.assertRaises(ValueError) as e:
            self.item.dimensions = (1, 2, -3)
        
        self.assertEqual(
            "Dimensions tuple must contain integers greater than zero.",
            str(e.exception))
        self.assertEqual((1, 2, 3), self.item.dimensions)
        
        with self.assertRaises(ValueError) as e:
            self.item.dimensions = (-1, -2, 3)
        
        self.assertEqual(
            "Dimensions tuple must contain integers greater than zero.",
            str(e.exception))
        self.assertEqual((1, 2, 3), self.item.dimensions)
        
        with self.assertRaises(ValueError) as e:
            self.item.dimensions = (-1, 2, -3)
        
        self.assertEqual(
            "Dimensions tuple must contain integers greater than zero.",
            str(e.exception))
        self.assertEqual((1, 2, 3), self.item.dimensions)
        
        with self.assertRaises(ValueError) as e:
            self.item.dimensions = (1, -2, -3)
        
        self.assertEqual(
            "Dimensions tuple must contain integers greater than zero.",
            str(e.exception))
        self.assertEqual((1, 2, 3), self.item.dimensions)
        
        with self.assertRaises(ValueError) as e:
            self.item.dimensions = (-1, -2, -3)
        
        self.assertEqual(
            "Dimensions tuple must contain integers greater than zero.",
            str(e.exception))
        self.assertEqual((1, 2, 3), self.item.dimensions)
    
    def test_negative_weight(self):
        with self.assertRaises(ValueError) as e:
            self.item.weight = -1
        
        self.assertEqual("Weight must be greater than zero.", str(e.exception))
        self.assertEqual(3.0, self.item.weight)
    
    def test_zero_weight(self):
        with self.assertRaises(ValueError) as e:
            self.item.weight = 0
        
        self.assertEqual("Weight must be greater than zero.", str(e.exception))
        self.assertEqual(3.0, self.item.weight)
    
    def test_get_available_status(self):
        self.item.in_stock = True
        res = self.item.get_available_status()
        self.assertEqual("Model: A is currently in stock.", res)
        
        self.item.in_stock = False
        res = self.item.get_available_status()
        self.assertEqual("Model: A is currently unavailable.", res)
    
    def test_get_specifications(self):
        res = self.item.get_specifications()
        self.assertEqual(
            "Model: A has the following dimensions: 1mm x 2mm x 3mm and weighs: 3.0",
            res)
        
        self.item.weight = None
        res = self.item.get_specifications()
        self.assertEqual(
            "Model: A has the following dimensions: 1mm x 2mm x 3mm and weighs: N/A",
            res)


if __name__ == '__main__':
    main()
