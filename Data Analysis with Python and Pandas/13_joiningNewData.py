import pandas as pd
import matplotlib.pyplot as plt
from functions import state_list, HPI_Benchmark, mortgage30
from matplotlib import style
style.use('fivethirtyeight')
import quandl as Quandl
api_key = open('apiKey.txt', 'r').read()


# getting the data
m30 = mortgage30()
hpi_data = pd.read_pickle('fiddy_states3.pickle')
hpi_bench = HPI_Benchmark()
print(m30.head())
# # joining the data
hpi_m30 = hpi_data.join(m30)
# printing correlations with added data
print(hpi_m30.corr()['m30'].describe())
