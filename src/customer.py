class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def can_afford_drink(self, drink):
        return drink.price <= self.wallet
    
    def buy_drink(self, drink, pub):
        if pub.pub_has_drink(drink):
            if self.can_afford_drink(drink):
                self.wallet -= drink.price
                pub.till += drink.price
            else:
                return "cannot afford"
        else:
            return "not in stock"
