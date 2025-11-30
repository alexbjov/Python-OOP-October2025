from unittest import TestCase, main

from project.truck_driver import TruckDriver


class TestTruckDrive(TestCase):
    def setUp(self):
        self.driver = TruckDriver("John", 10.0)
    
    def test_init(self):
        self.assertEqual("John", self.driver.name)
        self.assertEqual(10.0, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)
    
    def test_earned_money_raises(self):
        with self.assertRaises(ValueError) as e:
            self.driver.earned_money = -1
        self.assertEqual("John went bankrupt.", str(e.exception))
        self.assertEqual(0, self.driver.earned_money)
    
    def test_earned_money_success(self):
        self.driver.earned_money = 10
        self.assertEqual(10, self.driver.earned_money)
    
    def test_add_cargo_offer_failed(self):
        self.driver.available_cargos = {"SF": 10}
        with self.assertRaises(Exception) as e:
            self.driver.add_cargo_offer("SF", 10)
        
        self.assertEqual("Cargo offer is already added.", str(e.exception))
        self.assertEqual({"SF": 10}, self.driver.available_cargos)
    
    def test_add_cargo_offer_success(self):
        result = self.driver.add_cargo_offer("SF", 10)
        self.assertEqual("Cargo for 10 to SF was added as an offer.", result)
        self.assertEqual({"SF": 10}, self.driver.available_cargos)
        
        result = self.driver.add_cargo_offer("SA", 40)
        self.assertEqual("Cargo for 40 to SA was added as an offer.", result)
        self.assertEqual({"SF": 10, "SA": 40}, self.driver.available_cargos)
    
    def test_drive_best_cargo_offer_raises(self):
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", result)
        self.assertEqual({}, self.driver.available_cargos)
    
    def test_drive_best_cargo_offer_success(self):
        self.driver.available_cargos = {"SF": 10, "NY": 20}
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual("John is driving 20 to NY.", result)
        
        self.assertEqual(200, self.driver.earned_money)
        self.assertEqual(20, self.driver.miles)
        
        self.driver.add_cargo_offer("SA", 40)
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual("John is driving 40 to SA.", result)
        self.assertEqual(600, self.driver.earned_money)
        self.assertEqual(60, self.driver.miles)
    
    def test_eat_no_remainder(self):
        self.driver.earned_money = 250
        self.driver.eat(250)
        self.assertEqual(230, self.driver.earned_money)
    
    def test_eat_with_remainder(self):
        self.driver.earned_money = 250
        self.driver.eat(240)
        self.assertEqual(250, self.driver.earned_money)
        
        self.driver.eat(250)
        self.assertEqual(230, self.driver.earned_money)
    
    def test_sleep_no_remainder(self):
        self.driver.earned_money = 1000
        self.driver.sleep(1000)
        self.assertEqual(955, self.driver.earned_money)
    
    def test_sleep_with_remainder(self):
        self.driver.earned_money = 1000
        self.driver.sleep(900)
        self.assertEqual(1000, self.driver.earned_money)
        
        self.driver.sleep(1000)
        self.assertEqual(955, self.driver.earned_money)
    
    def test_pump_gas_no_remainder(self):
        self.driver.earned_money = 1500
        self.driver.pump_gas(1500)
        self.assertEqual(1000, self.driver.earned_money)
    
    def test_pump_gas_with_remainder(self):
        self.driver.earned_money = 1500
        self.driver.pump_gas(1400)
        self.assertEqual(1500, self.driver.earned_money)
        
        self.driver.pump_gas(1500)
        self.assertEqual(1000, self.driver.earned_money)
    
    def test_repair_truck_no_remainder(self):
        self.driver.earned_money = 10_000
        self.driver.repair_truck(10_000)
        self.assertEqual(2500, self.driver.earned_money)
    
    def test_repair_truck_with_remainder(self):
        self.driver.earned_money = 10_000
        self.driver.repair_truck(9_000)
        self.assertEqual(10_000, self.driver.earned_money)
        
        self.driver.repair_truck(10_000)
        self.assertEqual(2500, self.driver.earned_money)
    
    def test_repr(self):
        result = repr(self.driver)
        self.assertEqual("John has 0 miles behind his back.", result)
        self.driver.miles = 20
        result = repr(self.driver)
        self.assertEqual("John has 20 miles behind his back.", result)
    
    def test_check_activities(self):
        self.driver.earned_money = 20000 * self.driver.money_per_mile
        self.assertEqual(200_000, self.driver.earned_money)
        self.driver.check_for_activities(20000)
        self.assertEqual(176_000, self.driver.earned_money)


if __name__ == '__main__':
    main()
