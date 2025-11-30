from unittest import TestCase, main

from project.gallery import Gallery


class GalleryTest(TestCase):
    def setUp(self):
        self.gallery = Gallery("A23B", "Boston", 200.0)
    
    def test_init(self):
        self.assertEqual('A23B', self.gallery.gallery_name)
        self.assertEqual("Boston", self.gallery.city)
        self.assertEqual(200.0, self.gallery.area_sq_m)
        self.assertTrue(self.gallery.open_to_public)
        self.assertEqual({}, self.gallery.exhibitions)
        
        self.gallery.open_to_public = False
        self.assertFalse(self.gallery.open_to_public)
    
    def test_gallery_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.gallery.gallery_name = "A#1"
        self.assertEqual("Gallery name can contain letters and digits only!", str(ex.exception))
        self.assertEqual("A23B", self.gallery.gallery_name)
    
    def test_gallery_city_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.gallery.city = "#Boston"
        self.assertEqual("City name must start with a letter!", str(ex.exception))
        self.assertEqual("Boston", self.gallery.city)
    
    def test_area_zero_sq_m_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.gallery.area_sq_m = 0
        self.assertEqual("Gallery area must be a positive number!", str(ex.exception))
        self.assertEqual(200.0, self.gallery.area_sq_m)
    
    def test_area_less_than_zero_sq_m_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.gallery.area_sq_m = -1
        self.assertEqual("Gallery area must be a positive number!", str(ex.exception))
        self.assertEqual(200.0, self.gallery.area_sq_m)
    
    def test_add_exhibition_not_existing_name_success(self):
        actual_result = self.gallery.add_exhibition("A", 2024)
        self.assertEqual('Exhibition "A" added for the year 2024.', actual_result)
        self.assertIn("A", self.gallery.exhibitions)
    
    def test_add_exhibition_existing_name_failed(self):
        self.gallery.exhibitions["A"] = 2022
        actual_result = self.gallery.add_exhibition("A", 2024)
        self.assertEqual('Exhibition "A" already exists.', actual_result)
        self.assertIn("A", self.gallery.exhibitions)
        self.assertEqual(2022, self.gallery.exhibitions["A"])
    
    def test_remove_exhibition_not_existing_name_failed(self):
        actual_result = self.gallery.remove_exhibition("A")
        self.assertEqual('Exhibition "A" not found.', actual_result)
        self.assertEqual({}, self.gallery.exhibitions)
    
    def test_remove_exhibition_existing_name_success(self):
        self.gallery.exhibitions = {"A": 2024, "B": 2022}
        actual_result = self.gallery.remove_exhibition("A")
        self.assertEqual('Exhibition "A" removed.', actual_result)
        self.assertEqual({"B": 2022}, self.gallery.exhibitions)
    
    def test_list_exhibitions_open_to_public(self):
        self.gallery.exhibitions = {"A": 2024, "B": 2022}
        actual_result = self.gallery.list_exhibitions()
        self.assertEqual("A: 2024\nB: 2022", actual_result)
    
    def test_list_exhibitions_not_open_to_public(self):
        self.gallery.exhibitions = {"A": 2024, "B": 2022}
        self.gallery.open_to_public = False
        actual_result = self.gallery.list_exhibitions()
        self.assertEqual("Gallery A23B is currently closed for public! Check for updates later on.",
                         actual_result)


if __name__ == '__main__':
    main()
