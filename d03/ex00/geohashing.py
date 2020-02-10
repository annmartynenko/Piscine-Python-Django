import sys
import antigravity

def make_geohash():
	geohash = 0
	if len(sys.argv) < 1 or len(sys.argv) != 4:
		print("Wrong values")
	else:
		latitude = sys.argv[1]
		longtitude = sys.argv[2]
		date = sys.argv[3]
		geohash = antigravity.geohash(float(latitude), float(longtitude), date.encode('utf-8'))
	return geohash

if __name__ == '__main__':
	make_geohash()
