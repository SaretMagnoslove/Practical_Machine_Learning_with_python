import matplotlib.pyplot as plt

x = [2, 4, 6, 8, 10]
y = [6, 7, 8, 2, 4]

x2 = [1, 3, 5, 7, 9]
y2 = [7, 8, 2, 4, 2]

# plt.bar(x, y, label='bars1', color='r')
# plt.bar(x2, y2, label='bars2', color='c')


population_ages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]

bins = [x*10 for x in range(14)]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting graph\nCheck it out!')
plt.legend()

plt.show()

