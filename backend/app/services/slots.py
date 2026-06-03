from datetime import datetime, timedelta, time

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Booking
from app.schemas import TimeSlot


def _naive(dt: datetime) -> datetime:
    return dt.replace(tzinfo=None)


async def generate_slots(
    duration_minutes: int,
    date_from: datetime,
    date_to: datetime,
    db: AsyncSession,
) -> list[TimeSlot]:
    date_from = _naive(date_from)
    date_to = _naive(date_to)

    result = await db.execute(
        select(Booking).where(
            Booking.start_time < date_to,
            Booking.end_time > date_from,
        )
    )

    existing = [(_naive(b.start_time), _naive(b.end_time)) for b in result.scalars().all()]

    step = timedelta(minutes=duration_minutes)
    slots: list[TimeSlot] = []
    midnight = time(0, 0)
    one_day = timedelta(days=1)
    current_day = date_from

    while current_day < date_to:
        day_end = datetime.combine(current_day.date(), midnight) + one_day
        cursor = current_day

        while cursor + step <= day_end:
            slot_end = cursor + step
            overlap = any(
                existing_start < slot_end and existing_end > cursor
                for existing_start, existing_end in existing
            )
            if not overlap:
                slots.append(TimeSlot(start_time=cursor, end_time=slot_end))
            cursor += step

        current_day += one_day

    return slots
