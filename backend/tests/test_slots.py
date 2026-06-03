from datetime import datetime, timezone, timedelta

import pytest


@pytest.mark.asyncio
async def test_get_slots_nonexistent_event_type(client):
    resp = await client.get("/api/event-types/non-existent/slots")
    assert resp.status_code == 404


@pytest.mark.asyncio
async def test_get_slots_default_range(client):
    create_resp = await client.post(
        "/api/admin/event-types",
        json={"name": "Chat", "description": "x", "duration_minutes": 60},
    )
    et = create_resp.json()

    resp = await client.get(f"/api/event-types/{et['id']}/slots")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) > 0
    for slot in data:
        assert "start_time" in slot
        assert "end_time" in slot


@pytest.mark.asyncio
async def test_slots_exclude_booked_times(client):
    create_resp = await client.post(
        "/api/admin/event-types",
        json={"name": "Chat", "description": "x", "duration_minutes": 60},
    )
    et = create_resp.json()

    now = datetime.now(timezone.utc)
    tomorrow = (now + timedelta(days=1)).replace(hour=10, minute=0, second=0, microsecond=0)

    await client.post(
        "/api/bookings",
        json={
            "event_type_id": et["id"],
            "start_time": tomorrow.isoformat(),
        },
    )

    date_from = tomorrow.replace(hour=0, minute=0, second=0, microsecond=0)
    date_to = tomorrow + timedelta(days=1)

    resp = await client.get(
        f"/api/event-types/{et['id']}/slots",
        params={
            "date_from": date_from.isoformat(),
            "date_to": date_to.isoformat(),
        },
    )
    assert resp.status_code == 200
    data = resp.json()

    booked_start = tomorrow.replace(tzinfo=None)
    booked_end = (tomorrow + timedelta(hours=1)).replace(tzinfo=None)

    for slot in data:
        s = datetime.fromisoformat(slot["start_time"])
        e = datetime.fromisoformat(slot["end_time"])
        overlap = s < booked_end and e > booked_start
        assert not overlap, f"Slot {slot} overlaps with booking"
