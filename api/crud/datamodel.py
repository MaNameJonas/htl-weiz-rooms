from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    __abstract__ = True


class Room(Base):
    __tablename__ = 'room'

    room_id = Column(Integer, primary_key=True)
    name = Column(String)
    occupied = Column(Boolean, default=False)
    description = Column(String)

    def __repr__(self):
        return f"<Room(id={self.room_id}, name='{self.name}', occupied={self.occupied}, description='{self.description}')>"
