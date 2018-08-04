import matplotlib.pyplot as plt 

x = [i for i in range(10)]
y = [i for i in range(10)]



fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.plot(x, y)
ax1.annotate('Bad News!',(x[2],y[2]),
                xytext=(0.8, 0.9), textcoords='axes fraction',
                arrowprops = dict(facecolor='grey',color='grey'))

plt.show()