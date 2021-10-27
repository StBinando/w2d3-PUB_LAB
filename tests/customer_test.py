import unittest
from src.customer import Customer
from src.pub import Pub
from src.drink import Drink

class CustomerTest(unittest.TestCase):

    def setUp(self):
        self.customer1 = Customer("Russell", 10.00)
        self.customer2 = Customer("Stefano", 1.00)
        self.pub = Pub("Red Lion", 100, [])
        self.drink1 = Drink("orange juice", 2.50, 0)
        self.drink2 = Drink("beer", 6, 2)
        self.drinks = [self.drink1, self.drink2]
        self.pub2 = Pub("Purple Lion", 200, self.drinks)

    def test_customer_has_name(self):
        self.assertEqual("Russell", self.customer1.name)

    def test_customer_has_money(self):
        self.assertEqual(1.00, self.customer2.wallet)

    def test_customer_can_buy_drink_ok(self):
        self.customer1.buy_drink(self.drink1, self.pub2)
        self.assertEqual(self.customer1.wallet, 7.50)
        self.assertEqual(self.pub2.till, 202.5)