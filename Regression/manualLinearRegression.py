from statistics import mean
import numpy as np
import matplotlib.pyplot as plt

# defining the x's and the y's
xs = np.array([1, 2, 3, 4, 5, 6], dtype=np.float64)
ys = np.array([5, 4, 6, 5, 6, 7], dtype=np.float64)
# quick plot of the points of date we defined
plt.scatter(xs, ys)
plt.show()


# defining a function for finding the best fit slop for y = mx + b
def best_fit_slop(xs, ys):
    m = (((mean(xs) * mean(ys)) - mean(xs * ys)) / (np.power(mean(xs), 2) - mean(
        np.power(xs, 2))))
    return m


# running the function on the data we have
m = best_fit_slop(xs, ys)
# printing the best fit\ slope we just found
print('best fit slop is: {}'.format(m))