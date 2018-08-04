import matplotlib.pyplot as plt 
import matplotlib.dates as mdates 
import numpy as np 
import urllib


def graph_data(stock):

    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'

    source_code = urllib.request.urlopen(stock_price_url).read().decode()

    stock_data = []
    split_data = source_code.split('\n')

    for line in split_data[1:]:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'values' not in line:
                stock_data.append(line)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interesting graph\nCheck it out!')
    plt.legend()

    plt.show()

    date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,
                                                          delimiter=',',
                                                          unpack=True,
                                                          # %Y = full year. 2015
                                                          # %y = partial year 15
                                                          # %m = number month
                                                          # %d = number day
                                                          # %H = hours
                                                          # %M = minutes
                                                          # %S = seconds
                                                          # 12-06-2014
                                                          # %m-%d-%Y
                                                          converters={0: bytespdate2num('%Y-%m-%d')})
 graph_data('TSLA')                                                         