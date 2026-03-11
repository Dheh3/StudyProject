from dotenv import load_dotenv
import os
from fastapi import FastAPI

load_dotenv()
app = FastAPI()
# uvicorn main:app --reload

from routers.room_routes import room_router

app.include_router(room_router)

print(os.getenv("USER_TEST"))
print("="*30)
