import googlemaps
from datetime import datetime
from pprint import pprint

gmaps = googlemaps.Client(key='AIzaSyCZ6-Z8fWWztJO_1gaAG-N9LNNQS2YfWj0')

# Geocoding an address
geocode_result = gmaps.geocode('Boston')
pprint(geocode_result)
geocode_result = geocode_result[0]
if ("geometry" in geocode_result and "location" in geocode_result['geometry'] and
    "lat" in geocode_result['geometry']['location'] and "lng" in geocode_result['geometry']['location']):
    print("found coordinates in result")

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
# now = datetime.now()
# directions_result = gmaps.directions("Sydney Town Hall",
#                                      "Parramatta, NSW",
#                                      mode="transit",
#                                      departure_time=now)
