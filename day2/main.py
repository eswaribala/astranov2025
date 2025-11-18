from exceptions import EmailException
from supplychain.location.locationcontroller import add_location, location_list
from supplychain.region.regioncontroller import add_region, region_list    
from supplychain.customer.models import Customer


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

#print location and region lists
print("Locations Added:")
for loc in location_list:
    print(loc.show())

print("Regions Added:") 
for reg in region_list:
    print(reg.show())

#create for customer
#customer=Customer(customer_id=1, name="John Doe", email="john.doe@example.com")


#add individual and corporate customers
from supplychain.customer.individualcontroller import add_individual_customer   
from supplychain.customer.corporatecontroller import add_corporate_customer
#sample individual and corporate customers
try:
    individual1 = add_individual_customer(customer_id=1, name="John Doe", email="john.does@example.com", date_of_birth="1990-01-01", gender="Male")
    corporate1 = add_corporate_customer(customer_id=2, name="Acme Corp", email="contact@acmecorp.com", company_type="Corporation", tax_id="123456789")  
    print("Individual Customer Added:")
    print(vars(individual1))
    print("Corporate Customer Added:")
    print(vars(corporate1)) 
    #print discounts
    print(f"Individual Customer Discount: {individual1.calculate_discount()*100}%")
    print(f"Corporate Customer Discount: {corporate1.calculate_discount()*100}%")
    #print payment terms
    print(f"Payment Terms: {Customer.payment_terms}")
except EmailException as e:
    print(f"Error: {e}")    
except Exception as e:
    print(f"An unexpected error occurred: {e}") 