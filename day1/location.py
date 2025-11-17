# define a class to represent a geographical location
class Location:
    # initialize the location with code, name, latitude, and longitude
    def __init__(self, location_code: int, location_name: str, latitude: float, longitude: float):
        self._location_code = location_code
        self._location_name = location_name
        self._latitude = latitude
        self._longitude = longitude

    

    # getter and setter methods for location_name
    #assigning location name
    def set_location_code(self, location_code: int):
        self._location_code = location_code
    
    def get_location_code(self) -> int:
        return self.location_code
    
    
    def set_location_name(self, location_name: str):
        self._location_name = location_name
    
    def get_location_name(self) -> str:
        return self._location_name
    