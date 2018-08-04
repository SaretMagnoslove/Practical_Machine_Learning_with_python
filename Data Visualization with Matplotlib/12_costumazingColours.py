import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates
from matplotlib.dates import bytespdate2num


def graph_data(stock):

    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))

    # Unfortunately, Yahoo's API is no longer available
    # feel free to adapt the code to another source, or use this drop-in replacement.
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')
    for line in split_source[1:]:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)

    date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(
        stock_data,
        delimiter=',',
        unpack=True,
        converters={0: bytespdate2num('%Y-%m-%d')})

    ax1.plot_date(date, closep, '-', label='Price')
    ax1.plot([],[],lw=5, label='loss', color='r', alpha=0.5)
    ax1.plot([],[],lw=5, label='gain', color='g', alpha=0.5)
    ax1.fill_between(
        date,
        closep,
        closep[0],
        where=(closep > closep[0]),
        facecolor='g',
        alpha=0.5)
    ax1.fill_between(
    date,
    closep,
    closep[0],
    where=(closep < closep[0]),
    facecolor='r',
    alpha=0.5)

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax1.grid(True)
    ax1.xaxis.label.set_color('c')
    ax1.yaxis.label.set_color('r')
    ax1.set_yticks([i for i in range(0, 800, 50)])

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(stock)
    plt.legend()
    plt.subplots_adjust(
        left=0.09, bottom=0.2, right=0.94, top=0.9, wspace=0.2, hspace=0)
    plt.show()


graph_data('EBAY')
