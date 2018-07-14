import pandas as pd
import quandl

quandl.ApiConfig.api_key = "YtHWyqZPrpUA26JNZBnV"  # enter your api key
df = quandl.get('WIKI/GOOGL')  # setting Data Frame
# initial observation of data
print(df.head())
# choosing features
df = df[['Adj. Open',  'Adj. High',  'Adj. Low',  'Adj. Close', 'Adj. Volume']]
# defining relationships
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Low'] * 100
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
# final modeling of the Data Frame
df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]
# final observation of data
print(df.head())