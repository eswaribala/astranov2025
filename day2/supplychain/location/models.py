class Location:
    def __init__(self, code,name,latitude,longitude):
        self.__code = code    
        self.__name = name
        self.__latitude = latitude
        self.__longitude = longitude
    def show(self):
        return f"Location[code={self.__code}, name={self.__name}, latitude={self.__latitude}, longitude={self.__longitude}]"    