from faker import Faker
fake=Faker("en_IN")

#create first set of locations
location_set_1 = set()
for _ in range(10):
    location = fake.city()
    location_set_1.add(location)
#create second set of locations
location_set_2 = set()
for _ in range(10):
    location = fake.city()
    location_set_2.add(location)

print("Location Set 1:", location_set_1)
print("Location Set 2:", location_set_2)