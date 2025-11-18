import os
from dotenv import load_dotenv
load_dotenv()

MYSQL_USER:str=os.getenv("MYSQL_USER")
MYSQL_PASSWORD:str=os.getenv("MYSQL_PASSWORD")
MYSQL_HOST:str=os.getenv("MYSQL_HOST")
MYSQL_PORT:int=os.getenv("MYSQL_PORT")
MYSQL_DB:str=os.getenv("MYSQL_DB")
"""
print(f"MYSQL_USER: {MYSQL_USER}")
print(f"MYSQL_PASSWORD: {MYSQL_PASSWORD}")  
print(f"MYSQL_HOST: {MYSQL_HOST}")
print(f"MYSQL_PORT: {MYSQL_PORT}")
print(f"MYSQL_DB: {MYSQL_DB}")
"""
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"