import unittest
from src.pub import Pub

class PubTest(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("Red Lion", 100, [])

    def test_pub_has_name(self):
        self.assertEqual("Red Lion", self.pub.name)

    def test_till_has_cash(self):
        self.assertEqual(100, self.pub.till)

    def test_drinks_list_is_empy(self):
        self.assertEqual([], self.pub.drinks)