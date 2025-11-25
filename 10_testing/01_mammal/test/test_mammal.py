from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
	def setUp(self):
		self.mammal = Mammal("Jenny", "Cat", "Meow!")
	
	def test_init(self):
		self.assertEqual('Jenny', self.mammal.name)
		self.assertEqual('Cat', self.mammal.type)
		self.assertEqual('Meow!', self.mammal.sound)
		self.assertEqual('animals', self.mammal._Mammal__kingdom)
	
	def test_make_sound(self):
		result = self.mammal.make_sound()
		self.assertEqual('Jenny makes Meow!', result)
	
	def test_get_kingdom(self):
		result = self.mammal.get_kingdom()
		self.assertEqual('animals', result)
	
	def test_info(self):
		result = self.mammal.info()
		self.assertEqual('Jenny is of type Cat', result)


if __name__ == '__main__':
	main()
