from faker import Faker
from region import Region
from location import Location
fake=Faker("en_IN")

dict_region_location={}

regions=[]
locations=[]


for _ in range(1,3):
    region_code=fake.random_int(1,100)
    region_name=fake.state()
    poulation=fake.random_int(1000000,10000000)
    area=fake.random_int(1000,10000)
    region=Region(region_code,region_name,poulation,area)
    regions.append(region)
    locations=[]
    for i in range(1,4):
        location_code=fake.random_int(100,999)
        location_name=fake.city()
        longitude=fake.longitude()
        latitude=fake.latitude()
        location=Location(location_code,location_name,longitude,latitude)
        locations.append(location)
        #key pair mapping
    dict_region_location[region._id]=locations


#print region code and location name
for key,value in dict_region_location.items():
    print(f"Region Code: {key})")
    for loc in value:
        print(f"    Location Name: {loc.get_location_name()}")