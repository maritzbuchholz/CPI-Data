from pandas import DataFrame, Series
import urllib2

item_code = {}

for row in urllib2.urlopen("http://download.bls.gov/pub/time.series/cu/cu.item"):
	line = row.split()
	_ = line.pop(-1)
	_ = line.pop(-1)
	_ = line.pop(-1)
	item_code[line.pop(0)] = ' '.join(line[1:])

del item_code['item_code']

item_code = Series(item_code)
