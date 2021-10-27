import unittest
from src.customer import Customer

class CustomerTest(unittest.TestCase):

    def setUp(self):
        self.customer1 = Customer("Russell", 10.00)
        self.customer2 = Customer("Stefano", 1.00)

    def test_customer_has_name(self):
        self.assertEqual("Russell", self.customer1.name)

    def test_customer_has_money(self):
        self.assertEqual(1.00, self.customer2.wallet)