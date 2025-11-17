from faker import Faker
fake = Faker("en_IN")

product_code = fake.ean(length=13)
product_stock_quantity = fake.random_int(min=100, max=1000)
product_buffer_stock_quantity = fake.random_int(min=0, max=100)
print("Generated Product Code (EAN-13):", product_code)
print("Product Stock Quantity:", product_stock_quantity)
print("Product Buffer Stock Quantity:", product_buffer_stock_quantity)

#trigger production
if product_stock_quantity <= product_buffer_stock_quantity:
    print("Triggering production as stock is below or equal to buffer stock.")
else:
    print("No need to trigger production as stock is above buffer stock.")