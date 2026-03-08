from dotenv import load_dotenv
import os
from fastapi import FastAPI

load_dotenv()
app = FastAPI()

print(os.getenv("USER_TEST"))
print("="*30)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id:int, q:str | None = None):
    return {"item_id": item_id, "q": q}