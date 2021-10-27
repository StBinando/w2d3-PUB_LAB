class Drink:
    def __init__(self, name, price, alcohol_level):
        self.name = name
        self.price = price
        self.alcohol_level = alcohol_level

    def alcoholic_drink(self):
        return self.alcohol_level >= 3