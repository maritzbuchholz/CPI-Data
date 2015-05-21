import pandas as pd
import numpy as np
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import csv

cols = ['series_id', 'year', 'period', 'value']

pd.read_csv("http://download.bls.gov/pub/time.series/cu/cu.data.1.AllItems",
delim_whitespace=True)
