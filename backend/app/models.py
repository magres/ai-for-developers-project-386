import uuid
from datetime import datetime

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


def new_uuid() -> str:
    return str(uuid.uuid4())


class EventType(Base):
    __tablename__ = "event_types"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_uuid)
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(String(1000))
    duration_minutes: Mapped[int]

    bookings: Mapped[list["Booking"]] = relationship(back_populates="event_type")


class Booking(Base):
    __tablename__ = "bookings"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_uuid)
    event_type_id: Mapped[str] = mapped_column(ForeignKey("event_types.id"))
    start_time: Mapped[datetime] = mapped_column()
    end_time: Mapped[datetime] = mapped_column()

    event_type: Mapped["EventType"] = relationship(back_populates="bookings")
