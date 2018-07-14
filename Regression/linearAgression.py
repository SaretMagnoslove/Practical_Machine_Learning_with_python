import pandas as pd
import quandl
import math

quandl.ApiConfig.api_key = "YtHWyqZPrpUA26JNZBnV"  # enter your api key
df = quandl.get('WIKI/GOOGL')  # setting Data Frame
# initial observation of data
print(df.head())
# choosing features
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
# defining relationships
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Low'] * 100
df['PCT_change'] = (
    df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
# final modeling of the Data Frame
df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]
# final observation of data
print(df.head())
# creating the label: the Adj. Close will be the closing price 10% days into the future
forecast_col = 'Adj. Close'  # new col to adjust
df.fillna(value=-99999, inplace=True)  # dealing with NaN
forecast_out = int(math.ceil(
    0.01 * len(df)))  # defining # of days to forcast (10%)
df['label'] = df[forecast_col].shift(-forecast_out)  # the actual label
# print data frame with labels
print(df.head())
