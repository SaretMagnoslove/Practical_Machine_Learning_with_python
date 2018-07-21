import pandas as pd 
import matplotlib.pyplot as plt 
from functions import state_list
from matplotlib import style
style.use('fivethirtyeight')
import quandl as Quandl
api_key = open('apiKey.txt','r').read()

data = pd.read_pickle('pickle.pickle')
print(data.head())

# data.plot()
# plt.legend().remove()
# plt.show()

# df = data.pct_change()
# df.plot()
# plt.legend().remove()
# plt.show()

states = state_list()
print(states)
Data = pd.DataFrame()

for abbv in states:
    Data[abbv] = (data[abbv]-data[abbv][0]) / data[abbv][0] * 100.0

Data.to_pickle('final.pickle')

# Data.plot()
# plt.legend().remove()
# plt.show()

def HPI_Benchmark():
    df = Quandl.get("FMAC/HPI_USA", authtoken=api_key)
    df["Value"] = (df["Value"]-df["Value"][0]) / df["Value"][0] * 100.0
    return df

# fig = plt.figure()
# ax1 = plt.subplot2grid((1,1), (0,0))

HPI_data = pd.read_pickle('final.pickle')
# benchmark = HPI_Benchmark()
# HPI_data.plot(ax=ax1)
# benchmark.plot(color='k',ax=ax1, linewidth=10)

# plt.legend().remove()
# plt.show()
HPI_state_correlation = HPI_data.corr()
print(HPI_state_correlation)
print(HPI_state_correlation.describe())
