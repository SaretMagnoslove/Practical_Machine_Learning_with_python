import matplotlib.pyplot as plt
import csv
import numpy as np 

# part 1
''' 
x, y = [], []

with open('example.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))
'''

# part 2
x, y = np.loadtxt('example.csv', delimiter=',', unpack=True)

plt.plot(x, y, label='loaded from file')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting graph\nCheck it out!')
plt.legend()

plt.show()
