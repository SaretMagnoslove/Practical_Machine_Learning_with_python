from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np 

style.use('ggplot')

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [5, 6, 7, 8, 2, 5, 6, 3, 7, 2]
z = [1, 2, 6, 3, 2, 7, 3, 3, 7, 2]

x2 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
y2 = [-5, -6, -7, -8, -2, -5, -6, -3, -7, -2]
z2 = [1, 2, 6, 3, 2, 7, 3, 3, 7, 2]

x3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y3 = [5, 6, 7, 8, 2, 5, 6, 3, 7, 2]
z3 = np.zeros(10)

dx = np.ones(10)
dy = np.ones(10)
dz = [i for i in range(1,11)]

ax1.bar3d(x3, y3, z3, dx, dy, dz)

ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')

plt.show()