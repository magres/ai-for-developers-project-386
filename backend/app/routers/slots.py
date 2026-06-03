from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db
from app.models import EventType
from app.schemas import TimeSlot
from app.services.slots import generate_slots

router = APIRouter(tags=["Guest: Slots"])


@router.get("/api/event-types/{event_type_id}/slots", response_model=list[TimeSlot])
async def get_slots(
    event_type_id: str,
    date_from: datetime | None = None,
    date_to: datetime | None = None,
    db: AsyncSession = Depends(get_db),
):
    event_type = await db.get(EventType, event_type_id)
    if event_type is None:
        raise HTTPException(status_code=404, detail="Event type not found")

    now = datetime.now(timezone.utc)
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)

    date_from = (date_from or today_start).replace(tzinfo=None)
    date_to = (date_to or (date_from + timedelta(days=14))).replace(tzinfo=None)

    if date_from >= date_to:
        return []

    return await generate_slots(
        duration_minutes=event_type.duration_minutes,
        date_from=date_from,
        date_to=date_to,
        db=db,
    )
