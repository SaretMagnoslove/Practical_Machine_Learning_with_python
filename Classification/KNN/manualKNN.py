import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import warnings
from matplotlib import style
from collections import Counter

style.use('fivethirtyeight')

dataset = {'k': [[1, 2], [2, 3], [3, 1]], 'r': [[6, 5], [7, 7], [8, 6]]}
new_feature = [5, 7]

[[plt.scatter(ii[0], ii[1], s=100, color=i) for ii in dataset[i]]
 for i in dataset]
plt.scatter(new_feature[0], new_feature[1], s=200, color='g')

plt.show()


def k_nearest_neighbors(data, predict, k=3):
    warnings.warn(
        'value of k is less then number of groups') if len(data) >= k else ('')

    # knnalgos
    # return vote_result