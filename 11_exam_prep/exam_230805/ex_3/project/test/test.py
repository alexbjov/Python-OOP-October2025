from unittest import TestCase, main

from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):
    def setUp(self):
        self.car1 = SecondHandCar("Model 1", "Type 1", 10_000, 8_000.00)
    
    def test_init(self):
        self.assertEqual("Model 1", self.car1.model)
        self.assertEqual("Type 1", self.car1.car_type)
        self.assertEqual(10_000, self.car1.mileage)
        self.assertAlmostEqual(8_000.00, self.car1.price, 1)
        self.assertEqual([], self.car1.repairs)
    
    def test_set_price_rises(self):
        with self.assertRaises(ValueError) as e:
            self.car1.price = 1.0
        
        self.assertEqual("Price should be greater than 1.0!", str(e.exception))
        self.assertAlmostEqual(8_000.00, self.car1.price, 1)
        
        with self.assertRaises(ValueError) as e:
            self.car1.price = 0.0
        self.assertEqual("Price should be greater than 1.0!", str(e.exception))
        self.assertAlmostEqual(8_000.00, self.car1.price, 1)
    
    def test_set_mileage_raises(self):
        with self.assertRaises(ValueError) as e:
            self.car1.mileage = 100
        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(e.exception))
        self.assertEqual(10_000, self.car1.mileage)
        
        with self.assertRaises(ValueError) as e:
            self.car1.mileage = 90
        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(e.exception))
        self.assertEqual(10_000, self.car1.mileage)
    
    def test_set_promotional_price_raises(self):
        with self.assertRaises(ValueError) as e:
            self.car1.set_promotional_price(8_000.00)
        self.assertEqual("You are supposed to decrease the price!", str(e.exception))
        self.assertAlmostEqual(8_000.00, self.car1.price, 1)
        
        with self.assertRaises(ValueError) as e:
            self.car1.set_promotional_price(9_000.00)
        self.assertEqual("You are supposed to decrease the price!", str(e.exception))
        self.assertAlmostEqual(8_000.00, self.car1.price, 1)
    
    def test_set_promotional_price_success(self):
        result = self.car1.set_promotional_price(7_000.00)
        self.assertEqual("The promotional price has been successfully set.", result)
        self.assertAlmostEqual(7_000.00, self.car1.price, 1)
    
    def test_need_repair(self):
        result = self.car1.need_repair(5000.00, "Repair 1")
        self.assertEqual("Repair is impossible!", result)
        self.assertAlmostEqual(8_000.00, self.car1.price, 1)
        self.assertEqual([], self.car1.repairs)
        
        result = self.car1.need_repair(3000.00, "Repair 1")
        self.assertEqual("Price has been increased due to repair charges.", result)
        self.assertAlmostEqual(11_000.00, self.car1.price, 1)
        self.assertEqual(["Repair 1"], self.car1.repairs)
        
        result = self.car1.need_repair(1000.00, "Repair 2")
        self.assertEqual("Price has been increased due to repair charges.", result)
        self.assertAlmostEqual(12_000.00, self.car1.price, 1)
        self.assertEqual(["Repair 1", "Repair 2"], self.car1.repairs)
    
    def test_greater_than_failure(self):
        car2 = SecondHandCar("Model 2", "Type 2", 20_000, 7_000.00)
        result = self.car1 > car2
        self.assertEqual("Cars cannot be compared. Type mismatch!", result)
        
        car2 = SecondHandCar("Model 2", "Type 1", 20_000, 7_000.00)
        result = self.car1 > car2
        self.assertTrue(result)
    
    def test_str(self):
        result = str(self.car1)
        expected = "Model Model 1 | Type Type 1 | Milage 10000km\nCurrent price: 8000.00 | Number of Repairs: 0"
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
