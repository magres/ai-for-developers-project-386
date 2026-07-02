from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db
from app.models import EventType
from app.schemas import TimeSlot
from app.services.slots import generate_slots

router = APIRouter(tags=["Guest: Slots"])


@router.get("/api/event-types/{event_type_id}/slots", response_model=list[TimeSlot], response_model_by_alias=True)
async def get_slots(
    event_type_id: str,
    tz_name: str = Query(..., alias="timezone"),
    date_from: datetime | None = Query(None, alias="dateFrom"),
    date_to: datetime | None = Query(None, alias="dateTo"),
    db: AsyncSession = Depends(get_db),
):
    event_type = await db.get(EventType, event_type_id)
    if event_type is None:
        raise HTTPException(status_code=404, detail="Event type not found")

    now = datetime.now(timezone.utc)
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)

    if date_from is None:
        date_from = today_start
    if date_to is None:
        date_to = date_from + timedelta(days=14)

    if date_from >= date_to:
        return []

    return await generate_slots(
        duration_minutes=event_type.duration_minutes,
        date_from=date_from,
        date_to=date_to,
        tz_name=tz_name,
        db=db,
        now=now,
    )
