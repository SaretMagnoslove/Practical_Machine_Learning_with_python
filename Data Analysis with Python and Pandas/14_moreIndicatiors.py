import pandas as pd
import matplotlib.pyplot as plt
from functions import state_list, HPI_Benchmark, mortgage30, sp500, gdp, us_unemployment, stocks, women_emp
from matplotlib import style
style.use('fivethirtyeight')
import quandl
api_key = open('apiKey.txt', 'r').read()

# getting the data
m30 = mortgage30()
hpi_data = pd.read_pickle('fiddy_states3.pickle')
hpi_bench = HPI_Benchmark()
gdp = gdp()
stocks = stocks()
women_emp = women_emp()
# # # joining the data
hpi = hpi_data.join([m30, women_emp, gdp, stocks])
# # printing correlations with added data
hpi.dropna(inplace=True)
print(hpi.corr()['women_emp'].describe())
hpi.to_pickle('myHpi.pickle')