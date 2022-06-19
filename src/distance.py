import json
import urllib2
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="fk")


def getDistance(startLoc, endLoc, mode):
    '''
    return distance and transit time for given origin, destination and transit type
    :param startLoc: starting location as string
    :param endLoc: destination location as string
    :param mode: mode of transit as string
    :return: start destination distance
    '''
    print(startLoc, endLoc)

    info = [startLoc, endLoc, 0]

    if (startLoc == endLoc):
        info[2] = -1
        return info
    S = geolocator.geocode(startLoc)
    E = geolocator.geocode(endLoc)
    print(E.latitude)
    origins = str(S.latitude) + ',' + str(S.longitude)
    destinations = str(E.latitude) + ',' + str(E.longitude)
    url = 'https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins=' + origins + '&destinations=' + destinations + '&travelMode=' + mode + '&key='
    print(url)
    while True:
        try:
            # Get API response
            response = str(urllib2.urlopen(url).read())
        except IOError:
            pass  # Fall through to retry loop (next loop)
        else:
            # No IOError has occurred, so parse result
            result = json.loads(response.replace('\\n', ''))
            info[2] = result['resourceSets'][0]['resources'][0]['results'][0]['travelDistance']
            #time = result['resourceSets'][0]['resources'][0]['results'][0]['travelDuration']
        return info[2]


# Test call
print(getDistance('Aachen west', 'Dortmund haupt bahnhof', 'transit'))
