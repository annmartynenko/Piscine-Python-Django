class HotBeverage:
    def __init__(self, price=0.30, name="hot beverage"):
        self.price = price
        self.name = name

    def __str__(self):
        d = self.description()
        str1 = "name: " + str(self.name) + "\n"
        str2 = "price: " + str(self.price) + "\n"
        str3 = "description: " + str(d) + "\n"
        return str1 + str2 + str3

    def description(self):
        return "Just some hot water in a cup."


class Coffee(HotBeverage):
    price = 0.30
    name = "coffee"

    def description(self):
        return "A coffee, to stay awake."


class Tea(HotBeverage):
    price = 0.30
    name = "tea"


class Chocolate(HotBeverage):
    price = 0.50
    name = "chocolate"

    def description(self):
        return "Chocolate, sweet chocolate..."


class Cappuchino(HotBeverage):
    price = 0.45
    name = "cappuchino"

    def description(self):
        return "Un po’ di Italia nella sua tazza!"



