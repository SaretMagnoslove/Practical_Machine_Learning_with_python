from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

m = Basemap(
    projection='mill',
    llcrnrlat=-90,
    llcrnrlon=-180,
    urcrnrlat=90,
    urcrnrlon=180,
    resolution='l')
m.drawcoastlines()
m.drawcountries(linewidth=2)
m.drawstates(color='b')
m.drawcounties(color='darkred')
m.etopo()
m.bluemarble()

plt.title('Basemap Introduction')
plt.show()
