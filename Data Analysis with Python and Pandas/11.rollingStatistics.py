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
ax1 = plt.subplot2grid((2, 1), (0, 0))
ax2 = plt.subplot2grid((2, 1), (1, 0), sharex=ax1)

HPI_data = pd.read_pickle('final.pickle')
# HPI_data['TX12MA'] = pd.rolling_mean(HPI_data['TX'], 12)
# HPI_data['TX12Std'] = pd.rolling_std(HPI_data['TX'], 12)

# print(HPI_data[['TX', 'TX12MA']].head())
# # plotting the data
# HPI_data[['TX', 'TX12MA']].plot(ax=ax1)
# HPI_data['TX12Std'].plot(ax=ax2)
TX_AK_12corr = pd.rolling_corr(HPI_data['TX'], HPI_data['AK'], 12)

HPI_data['TX'].plot(ax=ax1, label='TX_HPI')
HPI_data['AK'].plot(ax=ax1, label='AK_HPI')
ax1.legend(loc=4)

TX_AK_12corr.plot(ax=ax2, label='TX_AK_12corr')

plt.legend(loc=4)
plt.show()
