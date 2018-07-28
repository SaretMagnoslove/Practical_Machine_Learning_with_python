import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [5, 7, 4]

x2 = [1, 2, 3]
y2 = [10, 14, 12]

plt.plot(x, y, label='first line')
plt.plot(x2, y2, label='second line')

plt.xlabel('plot number')
plt.ylabel('important var')

plt.title('Interesting graph\nCheck it out!')
plt.legend()

plt.show()
