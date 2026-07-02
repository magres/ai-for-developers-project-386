from datetime import datetime, timezone

from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db
from app.models import Booking, EventType
from app.schemas import BookingResponse, EventTypeCreate, EventTypeResponse

router = APIRouter(prefix="/api/admin", tags=["Admin"])


@router.post(
    "/event-types",
    response_model=EventTypeResponse,
    status_code=status.HTTP_201_CREATED,
    response_model_by_alias=True,
)
async def create_event_type(
    body: EventTypeCreate,
    db: AsyncSession = Depends(get_db),
):
    event_type = EventType(**body.model_dump())
    db.add(event_type)
    await db.commit()
    await db.refresh(event_type)
    return event_type


@router.get("/bookings", response_model=list[BookingResponse], response_model_by_alias=True)
async def list_upcoming_bookings(db: AsyncSession = Depends(get_db)):
    now = datetime.now(timezone.utc)
    result = await db.execute(
        select(Booking)
        .where(Booking.start_time >= now)
        .order_by(Booking.start_time)
    )
    return result.scalars().all()
