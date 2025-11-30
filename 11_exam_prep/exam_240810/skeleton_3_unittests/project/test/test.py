from unittest import TestCase, main

from project.soccer_player import SoccerPlayer


class TestSoccerPlayer(TestCase):
    def setUp(self):
        self.player1 = SoccerPlayer('Johnny', 21, 10, 'Real Madrid')
        self.player2 = SoccerPlayer('Michael', 23, 8, 'PSG')
    
    def test_init(self):
        self.assertEqual('Johnny', self.player1.name)
        self.assertEqual(21, self.player1.age)
        self.assertEqual(10, self.player1.goals)
        self.assertEqual('Real Madrid', self.player1.team)
        self.assertEqual({}, self.player1.achievements)
    
    def test_name_error(self):
        with self.assertRaises(ValueError) as e:
            self.player1.name = 'John'
        self.assertEqual('Name should be more than 5 symbols!',
                         str(e.exception))
        self.assertEqual('Johnny', self.player1.name)
        
        with self.assertRaises(ValueError) as e:
            self.player1.name = 'Peter'
        self.assertEqual('Name should be more than 5 symbols!',
                         str(e.exception))
        self.assertEqual('Johnny', self.player1.name)
    
    def test_age_error(self):
        with self.assertRaises(ValueError) as e:
            self.player1.age = 15
        self.assertEqual('Players must be at least 16 years of age!',
                         str(e.exception))
        self.assertEqual(21, self.player1.age)
    
    def test_goals(self):
        self.player1.goals = -1
        self.assertEqual(0, self.player1.goals)
        self.player1.goals = 5
        self.assertEqual(5, self.player1.goals)
    
    def test_team_error(self):
        with self.assertRaises(ValueError) as e:
            self.player1.team = 'Roma'
        self.assertEqual(
            'Team must be one of the following: Barcelona, Real Madrid, Manchester United, Juventus, PSG!',
            str(e.exception))
        self.assertEqual('Real Madrid', self.player1.team)
    
    def test_change_to_invalid_team(self):
        res = self.player1.change_team('Roma')
        self.assertEqual('Invalid team name!', res)
        self.assertEqual('Real Madrid', self.player1.team)
    
    def test_change_to_valid_team(self):
        res = self.player1.change_team('PSG')
        self.assertEqual('Team successfully changed!', res)
        self.assertEqual('PSG', self.player1.team)
    
    def test_add_new_achievement(self):
        res = self.player1.add_new_achievement('A')
        self.assertEqual(
            'A has been successfully added to the achievements collection!',
            res)
        self.assertEqual({'A': 1}, self.player1.achievements)
        res = self.player1.add_new_achievement('A')
        self.assertEqual(
            'A has been successfully added to the achievements collection!',
            res)
        self.assertEqual({'A': 2}, self.player1.achievements)
    
    def test_add_two_different_achievements(self):
        res = self.player1.add_new_achievement('A')
        self.assertEqual(
            'A has been successfully added to the achievements collection!',
            res)
        self.assertEqual({'A': 1}, self.player1.achievements)
        
        res = self.player1.add_new_achievement('B')
        self.assertEqual(
            'B has been successfully added to the achievements collection!',
            res)
        self.assertEqual({'A': 1, 'B': 1}, self.player1.achievements)
    
    def test_worse_goalscorer(self):
        res = self.player1 < self.player2
        self.assertEqual('Johnny is a better goal scorer than Michael.', res)
        res = self.player2 < self.player1
        self.assertEqual(
            'Johnny is a top goal scorer! S/he scored more than Michael.', res)


if __name__ == '__main__':
    main()
