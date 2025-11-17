#add the location
from location import Location
from faker import Faker

#faker instance
fake =Faker("en_IN")

# generate fake location data for 100 locations

locations = []
for _ in range(1,100):
    location_code = fake.unique.random_int(min=1000, max=9999)
    location_name = fake.city()
    latitude = float(fake.latitude())
    longitude = float(fake.longitude())
    location_object = Location(location_code, location_name, latitude, longitude)
    locations.append(location_object)

# print the location details
from_position=fake.random_int(min=0, max=98)
end_position=fake.random_int(min=from_position+1, max=99)
print(f"Displaying locations from position {from_position} to {end_position-1}:\n")
if from_position<end_position:
    for loc in locations[from_position:end_position]:
        print(f"Location Code: {loc._location_code}")
        print(f"Location Name: {loc._location_name}")    
        print(f"Latitude: {loc._latitude}")
        print(f"Longitude: {loc._longitude}")
        print("-----")









"""
#generate fake location data
location_code = fake.unique.random_int(min=1000, max=9999)
location_name = fake.city()
latitude = float(fake.latitude())
longitude = float(fake.longitude())
location_object=Location(location_code, location_name, latitude, longitude)


#print the location details
print(f"Location Code: {location_object._location_code}")
print(f"Location Name: {location_object._location_name}")    
print(f"Latitude: {location_object._latitude}")
print(f"Longitude: {location_object._longitude}")


#update location name
new_location_name = input("Enter new location name: ")
location_object.set_location_name(new_location_name)

#print the updated location name
print(f"Updated Location Name: {location_object.get_location_name()}")
"""