from collections import deque
from unittest import TestCase, main

from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):
    def setUp(self):
        self.station = RailwayStation("ABCD")
    
    def test_init(self):
        self.assertEqual("ABCD", self.station.name)
        self.assertEqual(deque(), self.station.arrival_trains)
        self.assertEqual(deque(), self.station.departure_trains)
    
    def test_name_length_equal_to_three(self):
        with self.assertRaises(ValueError) as e:
            self.station.name = "ABC"
        self.assertEqual("Name should be more than 3 symbols!",
                         str(e.exception))
    
    def test_name_length_less_to_three(self):
        with self.assertRaises(ValueError) as e:
            self.station.name = "A"
        self.assertEqual("Name should be more than 3 symbols!",
                         str(e.exception))
    
    def test_new_arrival_on_board(self):
        self.assertEqual(deque(), self.station.arrival_trains)
        self.station.new_arrival_on_board("Train 1")
        self.assertEqual(deque(['Train 1']), self.station.arrival_trains)
        self.station.new_arrival_on_board("Train 2")
        self.assertEqual(deque(['Train 1', 'Train 2']),
                         self.station.arrival_trains)
    
    def test_train_has_arrived_non_empty_arrived_trains(self):
        self.station.arrival_trains = deque(["Train 1", "Train 2"])
        result = self.station.train_has_arrived("Train 2")
        self.assertEqual("There are other trains to arrive before Train 2.",
                         result)
    
    def test_train_has_arrived_success(self):
        self.station.arrival_trains = deque(["Train 1"])
        result = self.station.train_has_arrived("Train 1")
        self.assertEqual(
            "Train 1 is on the platform and will leave in 5 minutes.", result)
        
        self.station.arrival_trains = deque(["Train 1", "Train 2"])
        result = self.station.train_has_arrived("Train 1")
        self.assertEqual(
            "Train 1 is on the platform and will leave in 5 minutes.", result)
    
    def test_train_has_left_true(self):
        self.station.departure_trains = deque(["Train 1"])
        result = self.station.train_has_left("Train 1")
        self.assertTrue(result)
        self.station.departure_trains = deque(["Train 1", "Train 2"])
        result = self.station.train_has_left("Train 1")
        self.assertTrue(result)
    
    def test_train_has_left_false(self):
        self.station.departure_trains = deque()
        result = self.station.train_has_left("Train 1")
        self.assertFalse(result)
        self.station.departure_trains = deque(["Train 1", "Train 2"])
        result = self.station.train_has_left("Train 2")
        self.assertFalse(result)


if __name__ == '__main__':
    main()
