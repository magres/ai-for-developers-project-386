from datetime import datetime, timedelta, time, timezone
from zoneinfo import ZoneInfo

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Booking
from app.schemas import TimeSlot


def _to_utc(dt: datetime) -> datetime:
    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


async def generate_slots(
    duration_minutes: int,
    date_from: datetime,
    date_to: datetime,
    tz_name: str,
    db: AsyncSession,
    now: datetime | None = None,
) -> list[TimeSlot]:
    tz = ZoneInfo(tz_name)
    date_from = _to_utc(date_from)
    date_to = _to_utc(date_to)
    now_utc = _to_utc(now) if now else date_from

    result = await db.execute(
        select(Booking).where(
            Booking.start_time < date_to,
            Booking.end_time > date_from,
        )
    )

    existing = [
        (_to_utc(b.start_time), _to_utc(b.end_time))
        for b in result.scalars().all()
    ]

    step = timedelta(minutes=duration_minutes)
    slots: list[TimeSlot] = []
    work_start = time(9, 0)
    work_end = time(17, 0)

    local_date = date_from.astimezone(tz).replace(
        hour=0, minute=0, second=0, microsecond=0
    )

    date_to_local = date_to.astimezone(tz)

    while local_date < date_to_local:
        day_start = local_date.replace(
            hour=work_start.hour, minute=work_start.minute
        )
        day_end = local_date.replace(
            hour=work_end.hour, minute=work_end.minute
        )

        cursor = max(now_utc.astimezone(tz), date_from.astimezone(tz), day_start)

        while cursor + step <= day_end:
            slot_end = cursor + step

            slot_start_utc = _to_utc(cursor)
            slot_end_utc = _to_utc(slot_end)

            if slot_end_utc <= now_utc:
                cursor += step
                continue

            overlap = any(
                es < slot_end_utc and ee > slot_start_utc
                for es, ee in existing
            )
            if not overlap:
                slots.append(TimeSlot(
                    start_time=slot_start_utc,
                    end_time=slot_end_utc,
                ))
            cursor += step

        local_date += timedelta(days=1)

    return slots
