from sqlalchemy import create_engine
from .database import Base,engine
from .models import Location
from fastapi import FastAPI

# Create the database tables
Base.metadata.create_all(bind=engine)

#create fastapi app
app = FastAPI()


@app.get("/")
def load_home():
    return {"message": "Welcome to the Location API"}