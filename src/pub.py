class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks
 
    def pub_has_drink(self, drink):
        return drink in self.drinks