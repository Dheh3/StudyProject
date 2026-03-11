from fastapi import APIRouter
from starlette.responses import HTMLResponse

room_router = APIRouter(prefix="/room", tags=["room"])

@room_router.get("/")
async def get_room():
    x= 1+1
    return {"message": "sala numero: {x}".format(x=x)}