from datetime import timedelta, datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db
from app.models import Booking, EventType
from app.schemas import BookingCreate, BookingResponse

router = APIRouter(prefix="/api/bookings", tags=["Guest: Bookings"])


def _naive(dt: datetime) -> datetime:
    return dt.replace(tzinfo=None)


@router.post("", response_model=BookingResponse, status_code=status.HTTP_201_CREATED)
async def create_booking(body: BookingCreate, db: AsyncSession = Depends(get_db)):
    event_type = await db.get(EventType, body.event_type_id)
    if event_type is None:
        raise HTTPException(status_code=404, detail="Event type not found")

    start_time = _naive(body.start_time)
    end_time = start_time + timedelta(minutes=event_type.duration_minutes)

    if end_time <= _naive(datetime.now(timezone.utc)):
        raise HTTPException(
            status_code=400,
            detail="Cannot book a slot in the past",
        )

    result = await db.execute(
        select(Booking).where(
            Booking.start_time < end_time,
            Booking.end_time > start_time,
        )
    )
    if result.first() is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="This time slot is already booked",
        )

    booking = Booking(
        event_type_id=body.event_type_id,
        start_time=start_time,
        end_time=end_time,
    )
    db.add(booking)
    await db.commit()
    await db.refresh(booking)
    return booking
