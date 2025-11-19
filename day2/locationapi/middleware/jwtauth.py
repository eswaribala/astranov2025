
from dotenv import load_dotenv
from fastapi import Request
import os
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))

class JWTAthenticationMiddleware:
    async def dispatch(self, request:Request, call_next):
       if request.url.path in ["/","/login", "/signup","/docs", "/openapi.json"]:
           response = await call_next(request)
           return response