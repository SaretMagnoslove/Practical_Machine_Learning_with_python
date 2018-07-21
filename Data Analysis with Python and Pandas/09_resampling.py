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

TXyear = HPI_data['TX'].resample('A')
print(TXyear.head())
HPI_data['TX'].plot(ax=ax1, label='Monthly')
TXyear.plot(ax=ax1, label='Yearly')

plt.legend(loc=4)
plt.show()

TXyear = HPI_data['TX'].resample('A', how='ohlc')
print(TXyear.head())
HPI_data['TX'].plot(ax=ax1, label='Monthly')
TXyear.plot(ax=ax1)

plt.legend(loc=4)
plt.show()

TXyear = HPI_data['TX'].resample('D', how='mean')
print(TXyear.head())
HPI_data['TX'].plot(ax=ax1, label='Monthly')
TXyear.plot(ax=ax1, label='Daily')

plt.legend(loc=4)
plt.show()