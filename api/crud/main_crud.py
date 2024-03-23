import logging
import sqlalchemy

from typing import List
from sqlalchemy.exc import SQLAlchemyError

from .datamodel import Base, Room


class HTL_Weiz_Room:
    def __init__(self):
        db_connection = sqlalchemy.create_engine("sqlite:///rooms.db")
        print("test")
        Base.metadata.create_all(db_connection)
        self.session_factory = sqlalchemy.orm.sessionmaker()
        self.session_factory.configure(bind=db_connection)
        self.session = self.session_factory()
        print("Database created successfully")

    def get_single_room(self, room_id: int) -> Room:
        try:
            room = self.session.query(Room).filter(Room.room_id == room_id).first()
            return room
        except SQLAlchemyError as e:
            logging.error(f"Error occurred while retrieving room: {e}")
            return None

    def get_rooms(self) -> List[Room]:
        try:
            rooms = self.session.query(Room).all()
            return rooms
        except SQLAlchemyError as e:
            logging.error(f"Error occurred while retrieving rooms: {e}")
            return []

    def update_room(self, room_id: int, updated_room_data: dict) -> bool:
        try:
            room = self.session.query(Room).filter(Room.room_id == room_id).first()
            if room:
                for key, value in updated_room_data.items():
                    setattr(room, key, value)
                self.session.commit()
                return True
            else:
                return False
        except SQLAlchemyError as e:
            logging.error(f"Error occurred while updating room: {e}")
            return False

    def create_room(self, room_data: dict) -> Room:
        try:
            new_room = Room(**room_data)
            self.session.add(new_room)
            self.session.commit()
            return new_room
        except SQLAlchemyError as e:
            logging.error(f"Error occurred while creating room: {e}")
            return None

    def delete_room(self, room_id: int) -> bool:
        try:
            room = self.session.query(Room).filter(Room.room_id == room_id).first()
            if room:
                self.session.delete(room)
                self.session.commit()
                return True
            else:
                return False
        except SQLAlchemyError as e:
            logging.error(f"Error occurred while deleting room: {e}")
            return False
