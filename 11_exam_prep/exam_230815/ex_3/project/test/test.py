from unittest import TestCase, main

from project.trip import Trip


class TestTrip(TestCase):
    def setUp(self):
        self.trip = Trip(6400.0, 2, True)
    
    def test_init(self):
        self.assertEqual(6400.0, self.trip.budget)
        self.assertEqual(2, self.trip.travelers)
        self.assertTrue(self.trip.is_family)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)
    
    def test_one_traveler_raises(self):
        with self.assertRaises(ValueError) as e:
            self.trip.travelers = 0
        self.assertEqual("At least one traveler is required!", str(e.exception))
    
    def test_three_travellers_success(self):
        self.trip.travelers = 3
        self.assertEqual(3, self.trip.travelers)
    
    def test_is_family_various_travelers(self):
        self.trip.travelers = 3
        self.assertTrue(self.trip.is_family)
        self.trip.is_family = False
        self.assertFalse(self.trip.is_family)
        self.trip.travelers = 1
        self.trip.is_family = False
        self.assertFalse(self.trip.is_family)
        self.trip.is_family = True
        self.assertFalse(self.trip.is_family)
    
    def test_book_a_trip_non_existing_destination(self):
        result = self.trip.book_a_trip("ABCD")
        self.assertEqual("This destination is not in our offers, please choose a new one!", result)
    
    def test_book_a_trip_existing_destination_failed(self):
        result = self.trip.book_a_trip("Brazil")
        self.assertEqual("Your budget is not enough!", result)
    
    def test_book_a_trip_existing_destination_success(self):
        result = self.trip.book_a_trip("Bulgaria")
        self.assertEqual("Successfully booked destination Bulgaria! Your budget left is 5500.00", result)
    
    def test_booking_status_empty(self):
        result = self.trip.booking_status()
        self.assertEqual("No bookings yet. Budget: 6400.00", result)
    
    def test_booking_status_success(self):
        result = [
            "Booked Destination: Australia",
            "Paid Amount: 10260.00",
            "Booked Destination: Brazil",
            "Paid Amount: 11160.00",
            "Booked Destination: New Zealand",
            "Paid Amount: 13500.00",
            "Number of Travelers: 2",
            "Budget Left: 65080.00"
        ]
        self.trip.budget = 100000.0
        self.trip.book_a_trip("New Zealand")
        self.trip.book_a_trip("Australia")
        self.trip.book_a_trip("Brazil")
        self.assertEqual("\n".join(result), self.trip.booking_status())


if __name__ == '__main__':
    main()
