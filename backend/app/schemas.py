from datetime import datetime

from pydantic import BaseModel, field_validator


class EventTypeCreate(BaseModel):
    name: str
    description: str
    duration_minutes: int

    @field_validator("duration_minutes")
    @classmethod
    def must_be_positive(cls, v: int) -> int:
        if v < 1:
            raise ValueError("duration_minutes must be positive")
        return v


class EventTypeResponse(BaseModel):
    id: str
    name: str
    description: str
    duration_minutes: int


class BookingCreate(BaseModel):
    event_type_id: str
    start_time: datetime


class BookingResponse(BaseModel):
    id: str
    event_type_id: str
    start_time: datetime
    end_time: datetime


class TimeSlot(BaseModel):
    start_time: datetime
    end_time: datetime
