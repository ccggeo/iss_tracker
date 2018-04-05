import urllib2
import json
import geocoder
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

#pip install geocoder
def getTrackingdata():

    response = urllib2.urlopen('http://api.open-notify.org/iss-now.json').read()
    json_obj = str(response)

    data = json.loads(json_obj)

    time = data['timestamp']
    timestamp = str(time)

    position = data['iss_position']

    longitude = position['longitude']
    latitude = position['latitude']
    #time related to position?

    g = geocoder.google([latitude, longitude], method='reverse')
    city = str(g.city)

    if city == 'None':
        print('Over ocean. No data')
    else:
        print('ISS is over ' + g.state_long + ', ' + g.country_long + ' ' + 'and the nearest city is ' + g.city)
    return longitude, latitude, timestamp

geolocation_data = getTrackingdata()

def drawMap(longitude, latitude):
	ax = plt.axes(projection=ccrs.Robinson())
	plt.title('ISS Position %s' % geolocation_data[2])
	img=plt.imread('bm.png')
	ax.imshow(img,origin='upper', transform=ccrs.PlateCarree())
	#ax.gridlines()

	plt.plot(longitude, latitude, 'ro'
			,transform=ccrs.PlateCarree(),
			)

	#plt.text(longitude +3,  latitude -12, 'iss position',
		#	horizontalalignment='left',
	#		transform=ccrs.Geodetic())

	plt.show()

drawMap(float(geolocation_data[0]), float(geolocation_data[1]))
