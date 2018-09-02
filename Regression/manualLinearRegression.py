from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random

style.use('fivethirtyeight')

# defining the x's and the y's
def create_dataset(hm, variance, step=2, correlation=False):
    val = 1
    ys = []
    for i in range(hm):
        y = val + random.randrange(-variance, variance)
        ys.append(y)
        if correlation and correlation == 'pos':
            val += step
        elif correlation and correlation == 'neg':
            val -= step
    xs = [i for i in range(len(ys))]

    return np.array(xs, dtype=np.float64), np.array(ys, dtype=np.float64)


# defining a function for finding the best fit slop for y = mx + b
def best_fit_slop_and_intercept(xs, ys):
    m = (((mean(xs) * mean(ys)) - mean(xs * ys)) /
         (np.power(mean(xs), 2) - mean(np.power(xs, 2))))
    b = mean(ys) - m * mean(xs)
    return m, b


def squared_error(y_orig, y_line):
    return sum((y_orig - y_line)**2)


def coefficient_of_determination(y_orig, y_line):
    y_mean_line = [mean(y_orig) for y in y_orig]
    squared_error_reg = squared_error(y_orig, y_line)
    squared_error_mean = squared_error(y_orig, y_mean_line)
    return 1 - (squared_error_reg / squared_error_mean)

xs, ys = create_dataset(40, 40, 2, correlation='pos')

# running the function on the data we have
m, b = best_fit_slop_and_intercept(xs, ys)
# printing the best fit\ slope we just found
print('best fit slop is: {} and the intercept is {}'.format(m, b))

regression_line = [m * x + b for x in xs]

# calculating r squared
r_squared = coefficient_of_determination(ys, regression_line)
print('r squared = {}'.format(r_squared))

# plotting the line
plt.scatter(xs,ys,color='#003F72', label = 'data')
plt.plot(xs, regression_line, label = 'regression line')
plt.legend(loc=4)
plt.show()