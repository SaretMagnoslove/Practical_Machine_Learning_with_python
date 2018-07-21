import pandas as pd

df = pd.read_csv('ZILLOW-Z77006.csv')
df.set_index('Date', inplace=True)
print(df.head())

df.to_csv('newcsv.csv')
df = pd.read_csv('newcsv.csv', index_col=0)
print(df.head())

df.columns = ['Austin_HPI']
print(df.head())

df.to_csv('newcsv2.csv', header=False)
df = pd.read_csv('newcsv2.csv', names=['Date', 'Austin_HPI'], index_col=0)
print(df.head())

df.to_html('example.html')
df = pd.read_csv('newcsv2.csv', names=['Date', 'Austin_HPI'])
df.rename(columns={'Austin_HPI': 'Aus_HPI'}, inplace=True)
print(df.head())