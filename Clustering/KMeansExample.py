import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
from sklearn.cluster import KMeans

x = np.random.randint(10, size=(60, 2))

# plt.scatter(x[:,0], x[:, 1])
# plt.show()

clf = KMeans(n_clusters=6)
clf.fit(x)

centroids = clf.cluster_centers_
labels = clf.labels_

colors = ['g.', 'r.', 'c.', 'b.', 'k.', 'orange']

for i in range(len(x)):
    plt.plot(x[i][0], x[i][1], colors[labels[i]], markersize=10)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=150, linewidths=5)
plt.show()
