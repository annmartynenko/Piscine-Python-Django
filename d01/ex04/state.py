import sys

def state():
	states = {
	"Oregon" : "OR",
	"Alabama" : "AL",
	"New Jersey": "NJ",
	"Colorado" : "CO"
	}
	capital_cities = {
	"OR": "Salem",
	"AL": "Montgomery",
	"NJ": "Trenton",
	"CO": "Denver"
	}
	if len(sys.argv) == 2:
		state = sys.argv[1]
		name = ''
		if state in capital_cities.values():
			for x in capital_cities:
				if state == capital_cities[x]:
					name = x
			for y in states:
				if name == states[y]:
					print(y)
		else:
			print("Unknown capital city")


if __name__ == '__main__':
	state()
