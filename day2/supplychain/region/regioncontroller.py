#add region

from supplychain.region.models import Region
region_list = []
def add_region(**details):
    for key,value in details.items():
        print(f"{key}: {value}")    
    region = Region(**details)
    region_list.append(region)
    return region_list