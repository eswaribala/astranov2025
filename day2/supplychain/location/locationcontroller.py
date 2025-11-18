#add the location
from supplychain.location.models import Location
location_list = []
def add_location(code, name, latitude, longitude):
    location = Location(code, name, latitude, longitude)
    location_list.append(location)
    return location_list