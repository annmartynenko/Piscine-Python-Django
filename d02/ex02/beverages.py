class HotBeverage:
	def __init__(self, price = 0.30, name = "hot beverage"):
		self.price = price
		self.name = name

	def __str__(self):
		d = self.description()
		str1 = "name: "+str(self.name)+"\n" 
		str2 = "price: "+"%.2f" % self.price+"\n"
		str3 = "description: "+str(d)+"\n"
		return str1 + str2 + str3

	def description(self):
		return "Just some hot water in a cup."


class Coffee(HotBeverage):
	def __init__(self):
		HotBeverage.__init__(self, 0.40, 'coffee')

	def description(self):
		return "A coffee, to stay awake."


class Tea(HotBeverage):
	def __init__(self):
		HotBeverage.__init__(self, 0.30, 'tea')


class Chocolate(HotBeverage):
	def __init__(self):
		HotBeverage.__init__(self, 0.50, 'chocolote')

	def description(self):
		return  "Chocolate, sweet chocolate..."


class Cappuchino(HotBeverage):
	def __init__(self):
		HotBeverage.__init__(self, 0.45, 'cappuchino')

	def description(self):
		return "Un po’ di Italia nella sua tazza!"
		

if __name__ == "__main__":
	coffee = Coffee()
	tea = Tea()
	chocolate = Chocolate()
	cappuchino = Cappuchino()
	print(coffee)
	print(tea)
	print(chocolate)
	print(cappuchino)
