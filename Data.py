import pandas as pd
from pandas import DataFrame, Series
import codes
import urllib2

cols = ['series_id', 'year', 'period', 'value']

data = pd.read_csv("http://download.bls.gov/pub/time.series/cu/cu.data.19.PopulationSize",
delim_whitespace=True, usecols=cols)

data['period'].replace(codes.period(), inplace=True)
data = data.merge(codes.s_id(), on='series_id')

print data
