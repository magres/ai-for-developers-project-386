from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db
from app.models import EventType
from app.schemas import EventTypeResponse

router = APIRouter(prefix="/api/event-types", tags=["Guest: Event Types"])


@router.get("", response_model=list[EventTypeResponse])
async def list_event_types(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(EventType).order_by(EventType.name))
    return result.scalars().all()
