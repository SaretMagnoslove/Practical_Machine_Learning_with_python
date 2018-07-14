import pandas as pd
import quandl, math
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

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
# making sure there are no Na
df.dropna(inplace=True)
# print data frame with labels
print(df.head())
# defining X as features and y as label
X = np.array(df.drop(['label'], 1))
y = np.array(df['label'])
# scaling X to be between -1 to 1
preprocessing.scale(X)
# only X's that has lablels (values for y)
# X = X[:-forecast_out+1] uneccessery already droped NaNs
print(len(X), len(y))  # making sure every X has a label
y = np.array(df['label'])
# creating train and test sets
X_train, X_test, y_train, y_test = cross_validation.train_test_split(
    X, y, test_size=0.2)
# defining the classifier
clf = LinearRegression(n_jobs=-1)
# training the clf.
clf.fit(X_train, y_train)
# testing the accuracy
accuracy = clf.score(X_test, y_test)
print(accuracy)
# compared to svm regression
clf = svm.SVR()
# training the clf.
clf.fit(X_train, y_train)
# testing the accuracy
accuracy = clf.score(X_test, y_test)
print(accuracy)
