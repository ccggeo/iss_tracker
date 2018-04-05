
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

ax = plt.axes(projection=ccrs.Robinson())
plt.title('ISS Position <date><time>')
img=plt.imread('/Users/cgeorge/bm.png')
ax.imshow(img,origin='upper', transform=ccrs.PlateCarree())
#ax.gridlines()

delhi_lon, delhi_lat = 0.127, 51.50

plt.plot(delhi_lon, delhi_lat, 'bo'
         ,transform=ccrs.PlateCarree(),
         )

plt.text(delhi_lon +3,  delhi_lat -12, 'London',
         horizontalalignment='left',
         transform=ccrs.Geodetic())

plt.show()

