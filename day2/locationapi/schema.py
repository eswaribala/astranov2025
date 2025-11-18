from pydantic import BaseModel

class LocationBase(BaseModel):
    name: str
    latitude: float
    longitude: float
    created_on: str  # ISO format date string

class LocationCreate(LocationBase):
    pass

