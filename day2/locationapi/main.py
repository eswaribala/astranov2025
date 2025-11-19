from sqlalchemy import create_engine
from database import Base
from fastapi import FastAPI
from database import engine
import uvicorn
# Create the database tables
Base.metadata.create_all(bind=engine)

#create fastapi app
app = FastAPI()


@app.get("/")
def load_home():
    return {"message": "Welcome to the Location API"}


if __name__ == "__main__":
    
    uvicorn.run(app, host="127.0.0.1", port=8000)