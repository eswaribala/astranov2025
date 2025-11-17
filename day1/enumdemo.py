from enum import Enum
import random

class Status(Enum):
    NEW = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    FAILED = 4

print ("Product Status")
print(random.choice(list(Status)))
status=Status.IN_PROGRESS
print(status)