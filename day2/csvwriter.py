import os
from models import User
from faker import Faker
faker=Faker("en_IN")
#create users
users=[]
for _ in range(10):
    username=faker.user_name()
    password=faker.password(length=10)
    user=User(username=username, password=password)
    users.append(user)
    
dirPath="E:\\astratraining\\day2\\reports\\"
fileName="users.csv"
if not os.path.exists(dirPath):
    os.makedirs(dirPath)

filePath = os.path.join(dirPath, fileName)
with open(filePath, mode='w', newline='') as file:
    file.write("id,username,email\n")
    for idx, user in enumerate(users, start=1):
        file.write(f"{idx},{user.username},{user.password}\n")

print(f"CSV file '{fileName}' created successfully at '{dirPath}'")
    