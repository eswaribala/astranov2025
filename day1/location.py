# define a class to represent a geographical location
class Location:
    def __init__(self, location_code: int, location_name: str, latitude: float, longitude: float):
        self.location_code = location_code
        self.location_name = location_name
        self.latitude = latitude
        self.longitude = longitude

    
