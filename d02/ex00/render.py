import sys, os, re
configfile_name = "settings.py"

def read_file():
	result = 0
	if os.path.isfile(configfile_name):
		cfgfile = open(configfile_name, 'r')
		sett = cfgfile.read()
		cfgfile.close()
	if len(sys.argv) == 2:
		file = sys.argv[1]
		check = re.search(r'.template', file)
		
		if (check and check.group() == '.template'):
			f = open(file, "r")
			text = f.read()
			f.close()
			lines = sett.split('\n')
			result = text
			for line in lines:
				name, val = line.split('=')
				name = name.strip()
				val = val.strip('"')
				result = re.sub('\{' + name + '\}', val, result)
		return result

def create_html(info):
	if info != 0:
		strResult = str(info)
		Html_file= open("myCV.html","w")
		Html_file.write(strResult)
		Html_file.close()

def render():
	info = read_file()
	create_html(info)

if __name__ == '__main__':
	render()
