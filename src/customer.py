class Customer:
    def __init__(self, name, wallet, age, drunkness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkness = drunkness

    def can_afford_drink(self, drink):
        return drink.price <= self.wallet

    def is_of_age(self, drink):
        if drink.alcoholic_drink():
            if self.age >= 18:
                return True
            else:
                return False
        else:
            return True   

    def is_not_drunk(self):
        return not(self.drunkness >= 10)

    def can_buy_drink(self, drink):
        return self.can_afford_drink(drink) and self.is_of_age(drink) and self.is_not_drunk()
        
    def buy_drink(self, drink, pub):
        if self.can_buy_drink(drink) and pub.pub_has_drink(drink):
            self.wallet -= drink.price
            pub.till += drink.price
            self.drunkness += drink.alcohol_level
        else:
            return "sorry pal"


