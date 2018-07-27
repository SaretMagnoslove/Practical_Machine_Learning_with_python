import quandl
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from statistics import mean
style.use('fivethirtyeight')


def create_labels(cur_hpi, fut_hpi):
    return 1 if fut_hpi > cur_hpi else 0


housing_data = pd.read_pickle('HPI.pickle')
housing_data = housing_data.pct_change()

housing_data.replace([np.inf, -np.inf], np.nan, inplace=True)
housing_data['US_HPI_future'] = housing_data['United States'].shift(-1)

housing_data.dropna(inplace=True)
# print(housing_data[['US_HPI_future', 'United States']].head())
# housing_data['label'] = list(
#     map(create_labels, housing_data['United States'],
#         housing_data['US_HPI_future']))
housing_data['label'] = [
    create_labels(fut, cur)
    for (cur, fut) in zip(housing_data['US_HPI_future'], housing_data['United States'])
    ]
print(housing_data.head())

