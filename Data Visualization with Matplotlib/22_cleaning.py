import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.dates import bytespdate2num
from matplotlib.finance import candlestick_ohlc
from matplotlib import style
import numpy as np
import urllib

# style.use('ggplot')
style.use('fivethirtyeight')

MA1 = 10
MA2 = 30


def moving_average(values, window):
    weights = np.repeat(1.0, window) / window
    smas = np.convolve(values, weights, 'valid')
    return smas


def highes_minus_lows(highs, lows):
    return highs - lows


def graph_data(stock):

    fig = plt.figure()
    ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=1, colspan=1)
    plt.title(stock)
    plt.ylabel('H-l')
    ax2 = plt.subplot2grid((6, 1), (1, 0), rowspan=4, colspan=1)
    plt.ylabel('Price')
    ax3 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1)
    plt.ylabel('MovingAvg')

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

    x, y, ohlc = 0, len(date), []

    while x < y:
        append_me = date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]
        ohlc.append(append_me)
        x += 1

    ma1 = moving_average(closep, MA1)
    ma2 = moving_average(closep, MA2)
    start = len(date[MA2 - 1:])

    h_l = [highes_minus_lows(h, l) for h, l in zip(highp, lowp)]
    # h_l = list(map(highes_minus_lows, highp, lowp))

    ax1.plot_date(date, h_l, '-')
    ax1.yaxis.set_major_locator(mticker.MaxNLocator(nbins=5, prune='lower'))

    candlestick_ohlc(ax2, ohlc, width=0.4, colorup='g', colordown='r')

    for label in ax2.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax2.grid(True)

    bbox_props = dict(boxstyle='larrow', fc='w', ec='k', lw=1)

    ax2.annotate(
        str(closep[-1]), (date[0], closep[-1]),
        xytext=(date[0] + 400, closep[-1]),
        bbox=bbox_props)

    ax3.plot(date[-start:], ma1[-start:], linewidth=1)
    ax3.plot(date[-start:], ma2[-start:], linewidth=1)

    ax3.fill_between(
        date[-start:],
        ma2[-start:],
        ma1[-start:],
        where=(ma1[-start:] < ma2[-start:]),
        facecolor='r',
        edgecolor='r',
        alpha=0.5)

    ax3.fill_between(
        date[-start:],
        ma2[-start:],
        ma1[-start:],
        where=(ma1[-start:] > ma2[-start:]),
        facecolor='g',
        edgecolor='g',
        alpha=0.5)

    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax3.xaxis.set_major_locator(mticker.MaxNLocator(10))

    for label in ax3.xaxis.get_ticklabels():
        label.set_rotation(45)

    plt.setp(ax1.get_xticklabels(), visible=False)
    plt.setp(ax2.get_xticklabels(), visible=False)
    plt.subplots_adjust(
        left=0.11, bottom=0.24, right=0.90, top=0.90, wspace=0.2, hspace=0)
    plt.show()


graph_data('EBAY')
