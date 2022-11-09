class Menu:
    def __init__(self, day = None, dish = None, total_price = 0, price = 0):
        self.day = day
        self.total_price = total_price
        self.dish = dish
        self.price = price
        self.list = []
    def buy(self):
        self.total_price += self.price
        return "ПІЦУ ПРИДБАНО"

    def add_ingredients(self, dish):
        list.append(dish)




