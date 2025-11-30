from unittest import TestCase, main

from project.toy_store import ToyStore


class ToyStoreTest(TestCase):
    def setUp(self):
        self.toy_store = ToyStore()
    
    def test_init(self):
        expected = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(expected, self.toy_store.toy_shelf)
    
    def test_add_toy_not_existing_shelf_raises(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A1", "doll")
        
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))
    
    def test_add_toy_in_the_shelf_raises(self):
        self.toy_store.toy_shelf['A'] = 'doll'
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "doll")
        self.assertEqual("Toy is already in shelf!", str(ex.exception))
    
    def test_add_another_toy_in_the_shelf_raises(self):
        self.toy_store.toy_shelf['A'] = 'doll'
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "car")
        self.assertEqual("Shelf is already taken!", str(ex.exception))
    
    def test_add_toy_success(self):
        result = self.toy_store.add_toy('A', 'doll')
        self.assertEqual("Toy:doll placed successfully!", result)
        self.assertEqual('doll', self.toy_store.toy_shelf['A'])
        
        result = self.toy_store.add_toy('B', 'car')
        self.assertEqual("Toy:car placed successfully!", result)
        self.assertEqual('doll', self.toy_store.toy_shelf['A'])
        self.assertEqual('car', self.toy_store.toy_shelf['B'])
    
    def test_remove_toy_not_existing_shelf_raises(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy('A1', 'doll')
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))
    
    def test_remove_toy_different_toy_raises(self):
        self.toy_store.toy_shelf['A'] = 'doll'
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy('A', 'truck')
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))
    
    def test_remove_toy_success(self):
        self.toy_store.toy_shelf['A'] = 'doll'
        actual = self.toy_store.remove_toy('A', 'doll')
        self.assertEqual("Remove toy:doll successfully!", actual)
        self.assertIsNone(self.toy_store.toy_shelf['A'])


if __name__ == '__main__':
    main()
