from pydantic import BaseModel


class RoomNoID(BaseModel):
    name: str
    occupied: bool
    description: str


class Room(RoomNoID):
    id: int
