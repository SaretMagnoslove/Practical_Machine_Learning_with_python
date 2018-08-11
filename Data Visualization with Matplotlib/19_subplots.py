import random
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()


def create_plots():
    xs = [x for x in range(10)]
    ys = [random.randrange(10) for _ in range(10)]
    return xs, ys


# add_subplot syntax:
# ax1 = fig.add_subplot(221)
# ax2 = fig.add_subplot(222)
# ax3 = fig.add_subplot(212)

# subplot2grid syntax:
ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=1, colspan=1)
ax2 = plt.subplot2grid((6, 1), (1, 0), rowspan=4, colspan=1)
ax3 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1)

x, y = create_plots()
ax1.plot(x, y)

x, y = create_plots()
ax2.plot(x, y)

x, y = create_plots()
ax3.plot(x, y)

plt.show()