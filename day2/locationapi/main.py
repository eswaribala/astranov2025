import http
from sqlalchemy import create_engine

from fastapi import FastAPI
from database import Base, engine, get_db
from locationapi.middleware.jwtauth import JWTAthenticationMiddleware
from models import Location
from schema import LocationCreate, LocationNameUpdate, LocationOut
from sqlalchemy.orm import Session
from fastapi import Depends,status
import uvicorn
# Create the database tables
Base.metadata.create_all(bind=engine)

#create fastapi app
app = FastAPI()
#add middleware
app.add_middleware(JWTAthenticationMiddleware)

@app.get("/")
def load_home():
    return {"message": "Welcome to the Location API"}


def jwt_login():
    pass

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
@app.get("/locations/v1.0/{code}", response_model=LocationOut)
def get_location_by_code(code:int, db:Session=Depends(get_db)):
    return db.query(Location).filter(Location.code==code).first()

@app.get("/locations/v1.0/name/{name}", response_model=list[LocationOut])
def get_location_by_name(name:str, db:Session=Depends(get_db)):
    return db.query(Location).filter(Location.name==name).all()

@app.patch("/locations/v1.0/{code}", response_model=LocationOut)
def update_location(code:int, location:LocationNameUpdate, db:Session=Depends(get_db)):
    db_location = db.query(Location).filter(Location.code==code).first()
    if db_location:
        db_location.name = location.name        
        db.commit()
        db.refresh(db_location)
    return db_location
@app.delete("/locations/v1.0/{code}", status_code=status.HTTP_204_NO_CONTENT)
def delete_location(code:int, db:Session=Depends(get_db)):
    db_location = db.query(Location).filter(Location.code==code).first()
    if db_location:
        db.delete(db_location)
        db.commit()
    return None


if __name__ == "__main__":
    
    uvicorn.run(app, host="127.0.0.1", port=8000)