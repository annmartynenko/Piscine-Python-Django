import sys

def read_file():
 	f = open("periodic_table.txt", "r")
 	text = f.read()
 	f.close()
 	text = text.split('\n')
 	x = 0
 	table = dict()
 	tmp = ''
 	for x in range((len(text)-1)):
 		tmp = text[x].split(',')
 		name = tmp[0].split('=')
 		number = tmp[1].split(':')
 		small = tmp[2].split(':')
 		molar = tmp[3].split(':')
 		electron = tmp[4].split(':')
 		position = name[1].split(':')
 		table[name[0]] = { position[0]:position[1], number[0]:number[1], small[0]:small[1], molar[0]:molar[1], electron[0]:electron[1] }
 	return table

def create_html(table):
	strPage = "<!DOCTYPE html><html lang='en'><head><title>Mendeleev's table</title><meta charset='utf-8'></head><body>"
	strTable = "<h2>Mendeleev's table</h2><table style='border:solid 1px pink;'>"
	pos = 0
	for a, b in table.items():
		if (int(b[' position']) == 0):
			strTwo = "<tr>"
			strTable = strTable + strTwo
		if (int(b[' position']) != pos + 1):
			for x in range(int(b[' position']) - pos - 1):
				strOne = "<td></td>"
				strTable = strTable+strOne
		if (b[' position'] != "17"):
			strOne = "<td style='border:solid 1px pink;'>"+"<h4>"+str(a)+"</h4>"
			strTwo = "<ul><li>"+str(b[' number'])+"</li><li>"+str(b[' small'])+"</li><li>"+str(b[' molar'])+"</li></ul>"+"</td>"
			strTable = strTable + strOne + strTwo
		if (b[' position'] == "17"):
			strOne = "<td style='border:solid 1px pink;'>"+"<h4>"+str(a)+"</h4>"
			strTwo = "<ul><li>"+str(b[' number'])+"</li><li>"+str(b[' small'])+"</li><li>"+str(b[' molar'])+"</li></ul>"+"</td></tr>"
			strTable = strTable + strOne + strTwo
		pos = int(b[' position'])
	strTable = strPage + strTable+"</table></body></html>"

	Html_file= open("periodic_table.html","w")
	Html_file.write(strTable)
	Html_file.close()

if __name__ == '__main__':
	table = read_file()
	create_html(table)
