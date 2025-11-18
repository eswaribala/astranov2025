#add the location
from location.models import Location
location_list = []
def add_location(code:str, name:str, latitude:float, longitude:float):
    location = Location(code, name, latitude, longitude)
    location_list.append(location)
    return location_list