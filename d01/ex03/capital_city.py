import sys

def city():
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
		if state in states:
			name = states.get(state)
			print(capital_cities.get(name))
		else:
			print("Unknown state")


if __name__ == '__main__':
	city()
