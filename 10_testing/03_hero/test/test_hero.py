from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero('Tom', 2, 50.0, 10.0)
    
    def test_init(self):
        self.assertEqual('Tom', self.hero.username)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(50.0, self.hero.health)
        self.assertEqual(10.0, self.hero.damage)
    
    def test_battle_cannot_fight_yourself_error(self):
        with self.assertRaises(Exception) as exc:
            self.hero.battle(self.hero)
        self.assertEqual('You cannot fight yourself', str(exc.exception))
    
    def test_battle_health_zero_or_less_error(self):
        self.hero.health = -1
        enemy_hero = Hero('John', 2, 30.0, 5.0)
        with self.assertRaises(ValueError) as exc:
            self.hero.battle(enemy_hero)
        self.assertEqual(
            'Your health is lower than or equal to 0. You need to rest',
            str(exc.exception))
        
        self.hero.health = 0
        with self.assertRaises(ValueError) as exc:
            self.hero.battle(enemy_hero)
        self.assertEqual(
            'Your health is lower than or equal to 0. You need to rest',
            str(exc.exception))
    
    def test_battle_enemy_health_zero_or_less_error(self):
        enemy_hero = Hero('John', 2, -1, 5.0)
        with self.assertRaises(ValueError) as exc:
            self.hero.battle(enemy_hero)
        self.assertEqual('You cannot fight John. He needs to rest',
                         str(exc.exception))
        
        enemy_hero.health = 0
        with self.assertRaises(ValueError) as exc:
            self.hero.battle(enemy_hero)
        self.assertEqual('You cannot fight John. He needs to rest',
                         str(exc.exception))
    
    def test_draw_game(self):
        self.hero = Hero('Tom', 2, 10.0, 10.0)
        enemy_hero = Hero('John', 2, 20.0, 5.0)
        self.assertEqual('Draw', self.hero.battle(enemy_hero))
    
    def test_win_game(self):
        self.hero = Hero('Tom', 2, 20.0, 10.0)
        enemy_hero = Hero('John', 2, 20.0, 5.0)
        self.assertEqual('You win', self.hero.battle(enemy_hero))
        self.assertEqual(3, self.hero.level)
        self.assertEqual(15.0, self.hero.health)
        self.assertEqual(15.0, self.hero.damage)
    
    def test_lose_game(self):
        self.hero = Hero('Tom', 2, 10.0, 10.0)
        enemy_hero = Hero('John', 3, 30.0, 10.0)
        self.assertEqual('You lose', self.hero.battle(enemy_hero))
        self.assertEqual(4, enemy_hero.level)
        self.assertEqual(15.0, enemy_hero.health)
        self.assertEqual(15.0, enemy_hero.damage)
    
    def test_str_method(self):
        result = f"Hero Tom: 2 lvl\nHealth: 50.0\nDamage: 10.0\n"
        self.assertEqual(result, str(self.hero))


if __name__ == '__main__':
    main()
