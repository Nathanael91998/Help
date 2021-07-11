'''
# importing googlemaps module
from googlemaps import Client as GoogleMaps
  
# Requires API key
gmaps = googlemaps.Client(key='Your_API_key')
  
# Requires cities name
my_dist = gmaps.distance_matrix('Delhi','Mumbai')['rows'][0]['elements'][0]
  
# Printing the result
print(my_dist)
'''
import pandas as pd
import numpy as np
restaurants = (
  pd.json_normalize(
    response,
    record_path = 'elements'
    ) 
)[['type', 'id', 'lat', 'lon', 'tags.amenity', 'tags.name', 'tags.cuisine']]
# since NaNs are not defined for characters in R (only for numeric)
# we need to replace NaNs for temporary 'NA' strings in python and
# then convert them to actual NAs in R
restaurants = restaurants.replace(np.nan, "NA")