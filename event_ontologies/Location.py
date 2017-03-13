"""This class is used to establish a Location object containing longitude, latitude, and address. This location will be
used to keep track of the place that an event occurs for the event web_scrapers

Copyright (c) 2017 Arjun Tanguturi (tanarj)
License: BSD 3
"""

from geopy.geocoders import Nominatim

class Location:
    
    def __init__(self, address = None):
        if address:
            geolocator = Nominatim()
            location = geolocator.geocode(address)
            self.address = location.address
            self.lat = location.latitude
            self.long = location.longitude

