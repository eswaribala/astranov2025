from faker import Faker
fake = Faker("en_IN")

product_code = fake.ean(length=13)
product_stock_quantity = fake.random_int(min=100, max=1000)
product_buffer_stock_quantity = fake.random_int(min=0, max=100)
product_stock_updated_on = fake.date_time_this_year()
print("Generated Product Code (EAN-13):", product_code)
print("Product Stock Quantity:", product_stock_quantity)
print("Product Buffer Stock Quantity:", product_buffer_stock_quantity)
print("Product Stock Updated On:", product_stock_updated_on)

#trigger production
if product_stock_quantity <= product_buffer_stock_quantity:
    print("Triggering production as stock is below or equal to buffer stock.")
else:
    print("No need to trigger production as stock is above buffer stock.")

# find out the last stock upate date difference from today
from datetime import datetime
today = datetime.now()
date_difference = (today - product_stock_updated_on).days
print("Days since last stock update:", date_difference)

if date_difference > 30:
    print("Stock update is older than 30 days. Consider reviewing stock levels.")
elif (date_difference > 15) and (date_difference <30):
    print("Stock update is older than 15 days. Monitor stock levels closely.")
else:
    print("Stock update is recent. No immediate action required.")