import sys

def all(state):
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
	name = ''
	if state in capital_cities.values():
		for x in capital_cities:
			if state == capital_cities[x]:
				name = x
		for y in states:
			if name == states[y]:
				print(state, "is the capital of", y)
				return 1
	elif state in states:
			name = states.get(state)
			print(capital_cities.get(name), "is the capital of", state)
			return 1
	else:
		return 0
		


def get_argv():
	if len(sys.argv) == 2:
		state = sys.argv[1]
		words = state.split(',')
		origin = words.copy()
		for x in range(len(words)):
			words[x] = words[x].strip()
			origin[x] = origin[x].strip()
			words[x] = words[x].casefold()
			words[x] = words[x].title()
		for i in range(len(words)):
	 		if words[i] != '':
	 			if(all(words[i]) == 0):
	 				print(origin[i], "is neither a capital city nor a state")	

if __name__ == '__main__':
	get_argv()