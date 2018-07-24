import pandas as pd
import matplotlib.pyplot as plt
from functions import state_list
from matplotlib import style
style.use('fivethirtyeight')
import quandl as Quandl
api_key = open('apiKey.txt', 'r').read()

data = pd.read_pickle('pickle.pickle')
# print(data.head())

states = state_list()
Data = pd.DataFrame()

# for abbv in states:
#     Data[abbv] = (data[abbv]-data[abbv][0]) / data[abbv][0] * 100.0

# Data.to_pickle('final.pickle')


def HPI_Benchmark():
    df = Quandl.get("FMAC/HPI_USA", authtoken=api_key)
    df["Value"] = (df["Value"] - df["Value"][0]) / df["Value"][0] * 100.0
    return df


fig = plt.figure()
ax1 = plt.subplot2grid((1, 1), (0, 0))

HPI_data = pd.read_pickle('final.pickle')
HPI_data['TX1yr'] = HPI_data['TX'].resample('A', how='mean')
print(HPI_data[['TX', 'TX1yr']])
# deleting the missing data
# HPI_data.dropna(inplace=True)
# deleting only if all the rows are NA
# HPI_data.dropna(how='all', inplace=True)
# setting a minimm threshold for number of NaNs
# HPI_data.dropna(thresh=0, inplace=True)
# filling data
# HPI_data.fillna(method='ffill', inplace=True)
# HPI_data.fillna(method='bfill', inplace=True)
# fill with certain value
# HPI_data.fillna(value=-99999, inplace=True)
# print(HPI_data.isnull().values.sum())
# HPI_data.fillna(value=0,limit=100,inplace=True)
# print(HPI_data.isnull().values.sum())
print(HPI_data[['TX', 'TX1yr']].head())
# plotting the data
HPI_data[['TX', 'TX1yr']].plot(ax=ax1)

plt.legend(loc=4)
plt.show()
