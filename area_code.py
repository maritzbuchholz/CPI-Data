from pandas import DataFrame, Series
import urllib2

area_code = {}

for row in urllib2.urlopen("http://download.bls.gov/pub/time.series/cu/cu.area"):
	line = row.split()
	_ = line.pop(-1)
	_ = line.pop(-1)
	_ = line.pop(-1)
	area_code[line.pop(0)] = ' '.join(line[1:])

del area_code['area_code']
 
area_code = Series(area_code)
