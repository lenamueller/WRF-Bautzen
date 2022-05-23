import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

from WRF_plot_domain import WRF_plot_domain # written by K. Barfus 20/09/2017 (Source: https://github.com/KlemensBarfus/WRF/blob/master/WRF_plot_domain.py)


# choose geo_em - files from WPS geogrid (one for each domain)
domain_names = ['modelfiles/geo_em.d01.nc','modelfiles/geo_em.d02.nc','modelfiles/geo_em.d03.nc']

map = Basemap(
    width=3500000,height=2800000,
    rsphere=(6378137.00,6356752.3142),
    resolution='l',
    area_thresh=5000.,
    projection='lcc', # Lambert Conformal Projection
    lat_1=51.22,lat_2=51.22, lat_0=51.22, # lat where projection area is tangent to earth surface = lat coordinate of Bautzen barrage
    lon_0=13.45 # lon coordinate of Bautzen barrage
  ) 

# add map elements
map.shadedrelief()
# map.drawmapboundary(fill_color='#9cc0fa')
# map.drawcoastlines(linewidth=0.3)
# map.drawcountries(linewidth=0.3, zorder=10)
# map.drawrivers(linewidth=0.5, color='#9cc0fa', zorder=3)
# map.fillcontinents(color='#f3ede2',lake_color='#9cc0fa')
map.drawmeridians(np.arange(0,360,10),color='k', linewidth=0.1, dashes=(None,None),labels=[0,0,0,1], size=8, zorder=1)
map.drawparallels(np.arange(-90,90,5),color='k', linewidth=0.1, dashes=(None, None),labels=[0,1,0,0], size=8, zorder=1)

# choose color for plotted domains
rgb = (1.0, 0.0, 0.0)

# plot domain to map
for i_domains in range(0, len(domain_names)):
  WRF_plot_domain(domain_names[i_domains], map, rgb, latname='XLAT_M', lonname='XLONG_M')

# annote labels for domains
plt.annotate('D1', xy=(0.27, 0.78), xycoords='axes fraction', fontsize=9, color='red')
plt.annotate('D2', xy=(0.37, 0.65), xycoords='axes fraction', fontsize=9, color='red')
plt.annotate('D3', xy=(0.46, 0.54), xycoords='axes fraction', fontsize=9, color='red')

# plot Bautzen barrage location to map
x, y = map(14.4565, 51.2151)
map.plot(x, y, marker='x',color='r', markersize=5)

# save plot
plt.savefig('processing/domains.png', dpi=500, bbox_inches='tight')
plt.close()