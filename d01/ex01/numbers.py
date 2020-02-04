def read_file():
 	f = open("numbers.txt", "r")
 	text = f.read()
 	f.close()
 	numbers = text.split(',')
 	for x in range(len(numbers)):
 		print(numbers[x])

if __name__ == '__main__':
	read_file()