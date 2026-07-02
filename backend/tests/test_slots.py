from datetime import datetime, timezone, timedelta

import pytest


TIMEZONE = "Asia/Yekaterinburg"


def _utc(*args) -> datetime:
    return datetime(*args, tzinfo=timezone.utc)


@pytest.mark.asyncio
async def test_get_slots_nonexistent_event_type(client):
    resp = await client.get("/api/event-types/non-existent/slots", params={"timezone": TIMEZONE})
    assert resp.status_code == 404


@pytest.mark.asyncio
async def test_get_slots_default_range(client):
    create_resp = await client.post(
        "/api/admin/event-types",
        json={"name": "Chat", "description": "x", "duration_minutes": 60},
    )
    et = create_resp.json()

    resp = await client.get(
        f"/api/event-types/{et['id']}/slots",
        params={"timezone": TIMEZONE},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) > 0
    for slot in data:
        assert "startTime" in slot
        assert "endTime" in slot


@pytest.mark.asyncio
async def test_slots_working_hours(client):
    create_resp = await client.post(
        "/api/admin/event-types",
        json={"name": "Chat", "description": "x", "duration_minutes": 60},
    )
    et = create_resp.json()

    now = datetime.now(timezone.utc)
    tomorrow = (now + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=timezone.utc)

    date_from = tomorrow
    date_to = tomorrow + timedelta(days=1)

    resp = await client.get(
        f"/api/event-types/{et['id']}/slots",
        params={
            "timezone": TIMEZONE,
            "date_from": date_from.isoformat(),
            "date_to": date_to.isoformat(),
        },
    )
    assert resp.status_code == 200
    data = resp.json()

    tz = __import__("zoneinfo").ZoneInfo(TIMEZONE)
    for slot in data:
        s = datetime.fromisoformat(slot["startTime"].replace("Z", "+00:00"))
        e = datetime.fromisoformat(slot["endTime"].replace("Z", "+00:00"))
        local_start = s.astimezone(tz)
        local_end = e.astimezone(tz)
        assert local_start.hour >= 9, f"Slot starts before 09:00: {slot}"
        assert local_end.hour <= 17 or (local_end.hour == 17 and local_end.minute == 0), \
            f"Slot ends after 17:00: {slot}"


@pytest.mark.asyncio
async def test_slots_exclude_booked_times(client):
    create_resp = await client.post(
        "/api/admin/event-types",
        json={"name": "Chat", "description": "x", "duration_minutes": 60},
    )
    et = create_resp.json()

    now = datetime.now(timezone.utc)
    tomorrow_start = (now + timedelta(days=1)).replace(
        hour=0, minute=0, second=0, microsecond=0, tzinfo=timezone.utc
    )

    tz = __import__("zoneinfo").ZoneInfo(TIMEZONE)
    booking_local = tomorrow_start.astimezone(tz).replace(hour=10, minute=0)
    booking_start = booking_local.astimezone(timezone.utc)

    await client.post(
        "/api/bookings",
        json={
            "event_type_id": et["id"],
            "start_time": booking_start.isoformat(),
        },
    )

    date_from = tomorrow_start
    date_to = tomorrow_start + timedelta(days=1)

    resp = await client.get(
        f"/api/event-types/{et['id']}/slots",
        params={
            "timezone": TIMEZONE,
            "date_from": date_from.isoformat(),
            "date_to": date_to.isoformat(),
        },
    )
    assert resp.status_code == 200
    data = resp.json()

    booked_end = booking_start + timedelta(hours=1)

    for slot in data:
        s = datetime.fromisoformat(slot["startTime"].replace("Z", "+00:00"))
        e = datetime.fromisoformat(slot["endTime"].replace("Z", "+00:00"))
        overlap = s < booked_end and e > booking_start
        assert not overlap, f"Slot {slot} overlaps with booking"
