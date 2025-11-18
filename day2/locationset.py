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

#union of two sets
union_set = location_set_1.union(location_set_2)
print("Union of Location Sets:", union_set)

#intersection of two sets
intersection_set = location_set_1.intersection(location_set_2)
print("Intersection of Location Sets:", intersection_set)
#difference of two sets
difference_set = location_set_1.difference(location_set_2)
print("Difference of Location Sets:", difference_set)