import unittest
from src.pub import Pub
from src.drink import Drink

class PubTest(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("Red Lion", 100, [])
        self.drink1 = Drink("orange juice", 2.50, 0)
        self.drink2 = Drink("beer", 6, 2)
        self.drinks = [self.drink1, self.drink2]
        self.pub2 = Pub("Purple Lion", 200, self.drinks)

    def test_pub_has_name(self):
        self.assertEqual("Red Lion", self.pub.name)

    def test_till_has_cash(self):
        self.assertEqual(100, self.pub.till)

    def test_drinks_list_is_empy(self):
        self.assertEqual([], self.pub.drinks)

    def test_pub2_has_drinks(self):
        self.assertEqual(2, len(self.pub2.drinks))

    def test_pub2_has_beer(self):
        self.assertTrue(self.pub2.pub_has_drink(self.drink2))
