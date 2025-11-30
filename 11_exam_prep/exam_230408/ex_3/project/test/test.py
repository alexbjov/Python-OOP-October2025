from unittest import TestCase, main

from project.tennis_player import TennisPlayer


class TestTennisPlayer(TestCase):
    def setUp(self):
        self.player1 = TennisPlayer("Peter", 20, 2300.0)
    
    def test_init(self):
        self.assertEqual("Peter", self.player1.name)
        self.assertEqual(20, self.player1.age)
        self.assertEqual(2300.0, self.player1.points)
        self.assertEqual([], self.player1.wins)
    
    def test_set_name(self):
        with self.assertRaises(ValueError) as e:
            self.player1.name = "Jo"
        self.assertEqual("Name should be more than 2 symbols!", str(e.exception))
        self.assertEqual("Peter", self.player1.name)
        
        with self.assertRaises(ValueError) as e:
            self.player1.name = "J"
        self.assertEqual("Name should be more than 2 symbols!", str(e.exception))
        self.assertEqual("Peter", self.player1.name)
    
    def test_set_age(self):
        with self.assertRaises(ValueError) as e:
            self.player1.age = 17
        self.assertEqual("Players must be at least 18 years of age!", str(e.exception))
        self.assertEqual(20, self.player1.age)
    
    def test_add_new_win(self):
        self.player1.add_new_win("Paris")
        self.assertEqual(["Paris"], self.player1.wins)
        
        self.player1.add_new_win("Rome")
        self.assertEqual(["Paris", "Rome"], self.player1.wins)
        
        result = self.player1.add_new_win("Paris")
        self.assertEqual("Paris has been already added to the list of wins!", result)
        self.assertEqual(["Paris", "Rome"], self.player1.wins)
    
    def test_less_than(self):
        player2 = TennisPlayer("John", 22, 2600.0)
        result = self.player1 < player2
        self.assertEqual("John is a top seeded player and he/she is better than Peter", result)
        
        player2.points = 2000.0
        result = self.player1 < player2
        self.assertEqual("Peter is a better player than John", result)
    
    def test_str_method(self):
        self.player1.wins = ["Paris", "Rome"]
        result = str(self.player1)
        self.assertEqual("Tennis Player: Peter\nAge: 20\nPoints: 2300.0\nTournaments won: Paris, Rome", result)


if __name__ == '__main__':
    main()
