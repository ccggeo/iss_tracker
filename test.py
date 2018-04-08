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
    print(longitude)
    print(latitude)
    #time related to position?
    try:
        g= geocoder.google([latitude, longitude], method='reverse')
        mapData = (g.raw)
        country=(mapData['country'])
        county = g.county
        print(county)
    except:
        g= (geocoder.google([latitude, longitude], method='reverse')).status
        print('Geocoder status is '+ g)

    return longitude, latitude, timestamp, country, county
getTrackingdata()
