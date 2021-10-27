import unittest
from src.drink import Drink

class DrinkTest(unittest.TestCase):

    def setUp(self):
        self.drink1 = Drink("orange juice", 2.50, 0)
        self.drink2 = Drink("beer", 6, 2)

    def test_drink_has_name(self):
        self.assertEqual("orange juice", self.drink1.name)

    def test_drink_has_price(self):
        self.assertEqual(2.50, self.drink1.price)

    def test_alcohol_level_is_2(self):
        self.assertEqual(2, self.drink2.alcohol_level)