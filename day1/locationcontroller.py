#add the location
from location import Location
from faker import Faker

#faker instance
fake =Faker("en_US")

#generate fake location data
location_code = fake.unique.random_int(min=1000, max=9999)
location_name = fake.city()
latitude = float(fake.latitude())
longitude = float(fake.longitude())
location_object=Location(location_code, location_name, latitude, longitude)


#print the location details
print(f"Location Code: {location_object.location_code}")
print(f"Location Name: {location_object.location_name}")    
print(f"Latitude: {location_object.latitude}")
print(f"Longitude: {location_object.longitude}")