import pandas as pd
from pandas import DataFrame, Series
import urllib2

def area_code():
	area_code = {}

	for row in urllib2.urlopen("http://download.bls.gov/pub/time.series/cu/cu.area"):
		line = row.split()
		_ = line.pop(-1)
		_ = line.pop(-1)
		_ = line.pop(-1)
		area_code[line.pop(0)] = ' '.join(line[1:])

	del area_code['area_code']
	 
	return Series(area_code)


def item_code():
	item_code = {}

	for row in urllib2.urlopen("http://download.bls.gov/pub/time.series/cu/cu.item"):
		line = row.split()
		_ = line.pop(-1)
		_ = line.pop(-1)
		_ = line.pop(-1)
		item_code[line.pop(0)] = ' '.join(line[1:])

	del item_code['item_code']

	return Series(item_code)


def periodicity_code():
	return Series({'R' : 'Monthly', 'S' : 'Semi-Annual'})


def s_id():
	cols = ['series_id', 'area_code', 'item_code', 'periodicity_code']

	s_id = pd.read_csv("http://download.bls.gov/pub/time.series/cu/cu.series",
	delim_whitespace=True, usecols=cols)

	#"Replacing Values" section in McKinny
	s_id['area_code'].replace(area_code(), inplace=True)
	s_id['item_code'].replace(item_code(), inplace=True)
	s_id['periodicity_code'].replace(periodicity_code(), inplace=True)
	return s_id


def period():
	period = {'M01' :	'January',
	'M02' :	'February',
	'M03' :	'March',
	'M04' :	'April',
	'M05' :	'May',
	'M06' :	'June',
	'M07' :	'July',
	'M08' :	'August',
	'M09' :	'September',
	'M10' :	'October',
	'M11' :	'November',
	'M12' : 'December',
	'M13' :	'Annual Average',
	'S01' :	'First Half',
	'S02' :	'Second Half',
	'S03' : 'Annual Average'}
	
	return Series(period)
	
