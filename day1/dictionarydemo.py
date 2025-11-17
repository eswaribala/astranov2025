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
    for _ in range(1,4):
        location_code=fake.random_int(100,999)
        location_name=fake.city()
        location=Location(location_code,location_name,region_code)
        locations.append(location)
        #key pair mapping
        dict_region_location[region._id]=location


