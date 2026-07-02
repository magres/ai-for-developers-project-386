from datetime import datetime, timezone

from pydantic import BaseModel, ConfigDict, field_validator, field_serializer


def to_camel(s: str) -> str:
    first, *rest = s.split("_")
    return first + "".join(w.capitalize() for w in rest)


def _ensure_utc(dt: datetime) -> str:
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.isoformat().replace("+00:00", "Z")


class CamelBase(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        from_attributes=True,
    )


class EventTypeCreate(CamelBase):
    name: str
    description: str
    duration_minutes: int

    @field_validator("duration_minutes")
    @classmethod
    def must_be_positive(cls, v: int) -> int:
        if v < 1:
            raise ValueError("duration_minutes must be positive")
        return v


class EventTypeResponse(CamelBase):
    id: str
    name: str
    description: str
    duration_minutes: int


class BookingCreate(CamelBase):
    event_type_id: str
    start_time: datetime


class BookingResponse(CamelBase):
    id: str
    event_type_id: str
    start_time: datetime
    end_time: datetime

    @field_serializer("start_time", "end_time")
    def serialize_dt(v: datetime) -> str:
        return _ensure_utc(v)


class TimeSlot(CamelBase):
    start_time: datetime
    end_time: datetime

    @field_serializer("start_time", "end_time")
    def serialize_dt(v: datetime) -> str:
        return _ensure_utc(v)
