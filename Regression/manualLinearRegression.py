from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

# defining the x's and the y's
xs = np.array([1, 2, 3, 4, 5, 6], dtype=np.float64)
ys = np.array([5, 4, 6, 5, 6, 7], dtype=np.float64)


# defining a function for finding the best fit slop for y = mx + b
def best_fit_slop_and_intercept(xs, ys):
    m = (((mean(xs) * mean(ys)) - mean(xs * ys)) /
         (np.power(mean(xs), 2) - mean(np.power(xs, 2))))
    b = mean(ys) - m * mean(xs)
    return m, b


# running the function on the data we have
m, b = best_fit_slop_and_intercept(xs, ys)
# printing the best fit\ slope we just found
print('best fit slop is: {} and the intercept is {}'.format(m, b))

regression_line = [m * x + b for x in xs]

# predicting y value for a new unseen x
predict_x = 8
predict_y = m * predict_x + b
plt.scatter(xs, ys)
plt.scatter(predict_x, predict_y, color='g')
plt.plot(xs, regression_line)
plt.show()