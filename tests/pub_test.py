import unittest
from src.pub import Pub

class PubTest(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("Red Lion", 100.00, {})

    def test_pub_has_name(self):
        self.assertEqual("Red Lion", self.pub.name)