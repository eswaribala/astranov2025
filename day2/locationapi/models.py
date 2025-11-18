
from sqlalchemy import Column, Integer, String, Float, Date
from .database import Base

class Location(Base):
    __tablename__ = "locations"
    code = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    created_on = Column(Date, nullable=False)