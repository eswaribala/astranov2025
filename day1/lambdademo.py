from faker import Faker
fake = Faker("en_IN")

ids=[]

for _ in range(10):
    ids.append(fake.unique.random_number(digits=10, fix_len=True))


#create lambda function handler

#string equals 9
tested_value=lambda id: id == "9"
for id in ids:
    convvalue = str(id)
    print(f"ID: {id}, Test Result: {tested_value(convvalue[0:1])}")