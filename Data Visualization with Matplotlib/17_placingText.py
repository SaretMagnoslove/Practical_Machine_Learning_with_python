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

    x, y, ohlc = 0, len(date), []

    while x < y:
        append_me = date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]
        ohlc.append(append_me)
        x += 1

    candlestick_ohlc(ax1, ohlc, width=0.4, colorup='g', colordown='r')

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax1.grid(True)
    # annotation example with arror
    ax1.annotate(
        'You are here!', (date[9], highp[9]),
        xytext=(0.8, 0.9),
        textcoords='axes fraction',
        arrowprops=dict(facecolor='grey', color='grey'))

    # font dic example
    font_dict = {'family': 'sherif', 'color': 'darkred', 'size': 15}
    # hard coded text
    ax1.text(date[4410], closep[1], 'Text Example', fontdict=font_dict)

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(stock)
    # plt.legend()
    plt.subplots_adjust(
        left=0.09, bottom=0.2, right=0.94, top=0.9, wspace=0.2, hspace=0)
    plt.show()


graph_data('EBAY')
