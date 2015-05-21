import pandas as pd
from pandas import DataFrame, Series
import codes
import urllib2

def s_id():
	cols = ['series_id', 'area_code', 'item_code', 'periodicity_code']

	s_id = pd.read_csv("http://download.bls.gov/pub/time.series/cu/cu.series",
	delim_whitespace=True, usecols=cols).set_index('series_id')

	#"Replacing Values" section in McKinny
	key['area_code'].replace(codes.area_code(), inplace=True)
	key['item_code'].replace(codes.item_code(), inplace=True)
	key['periodicity_code'].replace(codes.periodicity_code(), inplace=True)
	return s_id
