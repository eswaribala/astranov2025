#read location details from a user or faker
"""
Authors: Parameswari
Date: 2024-06-15    
Description: This module provides functions to generate or retrieve location details such as city, state, country, and postal code using the Faker library or user input.
"""

from faker import Faker
fake =Faker("en_IN")
location_code=fake.postcode()

print("Location Details:")
print("Location Code:", location_code)