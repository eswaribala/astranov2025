from supplychain.location.locationcontroller import add_location
from supplychain.region.regioncontroller import add_region
from faker import Faker
fake = Faker("en_IN")

# adding sample locations
#key pair in random order
add_location(latitude=28.6139, longitude=77.2090, code="DEL", name="New Delhi")
add_location(name="Mumbai", code="BOM", longitude=72.8777, latitude=19.0760)
add_location(code="BLR", name="Bangalore", latitude=12.9716, longitude=77.5946)

# adding sample regions
# key pair in random order and using **kwargs
add_region(name="North India", code="NI")   
add_region(code="SI")
add_region(name="South India")

