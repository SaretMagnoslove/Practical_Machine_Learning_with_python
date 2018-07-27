import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from statistics import mean
from sklearn import svm, preprocessing, cross_validation
style.use('fivethirtyeight')


def create_labels(cur_hpi, fut_hpi):
    return 1 if fut_hpi > cur_hpi else 0


housing_data = pd.read_pickle('HPI.pickle')
housing_data = housing_data.pct_change()

housing_data.replace([np.inf, -np.inf], np.nan, inplace=True)
housing_data['US_HPI_future'] = housing_data['United States'].shift(-1)

housing_data.dropna(inplace=True)
housing_data['label'] = [
    create_labels(fut, cur)
    for (cur, fut
         ) in zip(housing_data['US_HPI_future'], housing_data['United States'])
]

# features and labels
X = np.array(housing_data.drop(['label', 'US_HPI_future'], axis=1))
X = preprocessing.scale(X)
y = np.array(housing_data['label'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(
    X, y, test_size=0.2)
# train and test
clf = svm.SVC(kernel='linear')
clf.fit(X_train, y_train)
# checking the accuracy
print(clf.score(X_test, y_test))
