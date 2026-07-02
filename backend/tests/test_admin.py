from datetime import datetime, timezone, timedelta

import pytest


@pytest.mark.asyncio
async def test_admin_bookings_empty(client):
    resp = await client.get("/api/admin/bookings")
    assert resp.status_code == 200
    assert resp.json() == []


@pytest.mark.asyncio
async def test_admin_bookings_shows_upcoming(client):
    et_resp = await client.post(
        "/api/admin/event-types",
        json={"name": "Chat", "description": "x", "duration_minutes": 30},
    )
    et = et_resp.json()

    future = (datetime.now(timezone.utc) + timedelta(days=1)).replace(
        hour=10, minute=0, second=0, microsecond=0, tzinfo=timezone.utc
    )

    await client.post(
        "/api/bookings",
        json={"event_type_id": et["id"], "start_time": future.isoformat()},
    )

    resp = await client.get("/api/admin/bookings")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) == 1
    assert data[0]["eventTypeId"] == et["id"]
