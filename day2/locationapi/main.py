import http
from sqlalchemy import create_engine

from fastapi import FastAPI
from database import Base, engine, get_db
from models import Location
from schema import LocationCreate, LocationOut
from sqlalchemy.orm import Session
from fastapi import Depends,status
import uvicorn
# Create the database tables
Base.metadata.create_all(bind=engine)

#create fastapi app
app = FastAPI()


@app.get("/")
def load_home():
    return {"message": "Welcome to the Location API"}

@app.post("/locations/v1.0/", response_model=LocationOut, status_code=status.HTTP_201_CREATED)
def create_location(location:LocationCreate, db:Session=Depends(get_db)):
    db_location = Location(name=location.name, latitude=location.latitude, longitude=location.longitude, created_on=location.created_on)
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location

@app.get("/locations/v1.0/", response_model=list[LocationOut])
def get_locations(db:Session=Depends(get_db)):
    locations = db.query(Location).all()
    return locations

if __name__ == "__main__":
    
    uvicorn.run(app, host="127.0.0.1", port=8000)