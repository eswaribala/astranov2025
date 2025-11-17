#read location details from a user or faker
"""
Authors: Parameswari
Date: 2024-06-15    
Description: This module provides functions to generate or retrieve location details such as city, state, country, and postal code using the Faker library or user input.
"""

from faker import Faker
fake =Faker("en_IN")
location_code=fake.postcode()
location_name=fake.city()
location_coords=fake.local_latlng(country_code="IN", coords_only=True)


print("Location Details:")
print("Location Code:", location_code)
print("Location Name:", location_name)
print("Location Coordinates:", location_coords)

print(f"Name: {location_name}, Code: {location_code}, Coordinates: {location_coords}")

# identify variable types
print("Variable Types:")
print("Type of location_code:", type(location_code))
print("Type of location_name:", type(location_name))
print("Type of location_coords:", type(location_coords))