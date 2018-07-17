import pandas as pd
import quandl, math, datetime
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
import pickle

style = 'ggplot'

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

# new col to adjust
forecast_col = 'Adj. Close'
# dealing with NaN
df.fillna(value=-99999, inplace=True)
# defining # of days to forcast (10%)
forecast_out = int(math.ceil(0.01 * len(df)))
# the actual label
df['label'] = df[forecast_col].shift(-forecast_out)
# X for features and y for label
X = np.array(df.drop(['label'], 1))
X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
X = X[:-forecast_out]

df.dropna(inplace=True)

y = np.array(df['label'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(
    X, y, test_size=0.2)
# clf = LinearRegression(n_jobs=-1)
# clf.fit(X_train, y_train)
# # saving trained model into pickle
# with open('linearRegression.pickle','wb') as f:
#     pickle.dump(clf, f)
# loading trained model from pickle
pickle_in = open('linearRegression.pickle','rb')
clf = pickle.load(pickle_in)

accuracy = clf.score(X_test, y_test)
print(accuracy)
forecast_set = clf.predict(X_lately)
df['Forecast'] = np.nan

last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += 86400
    df.loc[next_date] = [np.nan for _ in range(len(df.columns) - 1)] + [i]

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show(1)