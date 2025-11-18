from pydantic import BaseModel

class LocationBase(BaseModel):
    name: str
    latitude: float
    longitude: float
    created_on: str  # ISO format date string

class LocationCreate(LocationBase):
    pass

class LocationUpdate(LocationBase):
    pass

class LocationDelete(LocationBase):
    pass
class Location(LocationBase):
    code: int

    class Config:
        orm_mode = True

