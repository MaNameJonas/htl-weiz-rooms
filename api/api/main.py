from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from api.crud.main_crud import HTL_Weiz_Room
from api.api.types import Room, RoomNoID


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8081",
    "http://localhost:8000",
    "http://localhost:5173",
    "http://localhost:5173/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

room_crud = HTL_Weiz_Room()


@app.get('/')
async def read_main():
    return "This is a tool to administrate th rooms of the HTL Weiz."


@app.get('/rooms/', tags=['rooms'])
async def read_rooms() -> List[Room]:
    rooms = room_crud.get_rooms()
    # Convert each room object to a dictionary and include the id field
    return [{**room.__dict__, 'id': room.room_id} for room in rooms]

@app.get('/rooms/{room_id}', tags=['rooms'])
async def read_room(room_id: int) -> Room:
    room = room_crud.get_single_room(room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    # Convert the room object to a dictionary and include the id field
    return {**room.__dict__, 'id': room.room_id}


@app.post('/rooms/', tags=['rooms'])
async def create_room(room: RoomNoID) -> Room:
    new_room = room_crud.create_room(room.dict())
    if not new_room:
        raise HTTPException(status_code=500, detail="Failed to create room")
    return new_room


@app.put('/rooms/{room_id}', tags=['rooms'])
async def update_room(room_id: int, room: RoomNoID) -> Room:
    updated_room = room_crud.update_room(room_id, room.dict())
    if not updated_room:
        raise HTTPException(status_code=404, detail="Room not found")
    return updated_room


@app.delete('/rooms/{room_id}', tags=['rooms'])
async def delete_room(room_id: int):
    deleted = room_crud.delete_room(room_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Room not found")
    return {"message": "Room deleted successfully"}
