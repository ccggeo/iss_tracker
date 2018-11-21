# https://python-graph-gallery.com/315-a-world-map-of-surf-tweets/
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

    g= geocoder.google([latitude, longitude], method='reverse')
    print(g.status)
    try:
        mapData = (g.raw)
        country_=(mapData['country'])
        country=str([country_['long_name']])
        county = g.county
    except:
        country = ''
        county=''
    return longitude, latitude, timestamp, country, county


geolocationData = getTrackingdata()
def drawMap(longitude, latitude):
    ax = plt.axes(projection=ccrs.Robinson())
    plt.title('ISS Global Positioning %s' % geolocationData[2])
    img=plt.imread('bm.png')
    ax.imshow(img,origin='upper', transform=ccrs.PlateCarree())
    #ax.gridlines()

    plt.plot(longitude, latitude, 'ro'
             ,transform=ccrs.PlateCarree(),
             )

    plt.text(longitude +3,  latitude -6, geolocationData[3] ,
             horizontalalignment='left', color='red',
             transform=ccrs.Geodetic())

    plt.show()

drawMap(float(geolocationData[0]), float(geolocationData[1]))
