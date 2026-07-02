from datetime import datetime, timezone, timedelta

import pytest


@pytest.mark.asyncio
async def test_create_booking(client):
    et_resp = await client.post(
        "/api/admin/event-types",
        json={"name": "Chat", "description": "x", "duration_minutes": 30},
    )
    et = et_resp.json()

    future = (datetime.now(timezone.utc) + timedelta(days=1)).replace(
        hour=10, minute=0, second=0, microsecond=0, tzinfo=timezone.utc
    )

    resp = await client.post(
        "/api/bookings",
        json={"event_type_id": et["id"], "start_time": future.isoformat()},
    )
    assert resp.status_code == 201
    data = resp.json()
    assert data["eventTypeId"] == et["id"]
    assert "id" in data
    assert "endTime" in data


@pytest.mark.asyncio
async def test_create_booking_nonexistent_event_type(client):
    future = (datetime.now(timezone.utc) + timedelta(days=1)).isoformat()
    resp = await client.post(
        "/api/bookings",
        json={"event_type_id": "bad-id", "start_time": future},
    )
    assert resp.status_code == 404


@pytest.mark.asyncio
async def test_double_booking_conflict(client):
    et_resp = await client.post(
        "/api/admin/event-types",
        json={"name": "Chat", "description": "x", "duration_minutes": 30},
    )
    et = et_resp.json()

    future = (datetime.now(timezone.utc) + timedelta(days=1)).replace(
        hour=10, minute=0, second=0, microsecond=0, tzinfo=timezone.utc
    )
    payload = {"event_type_id": et["id"], "start_time": future.isoformat()}

    resp1 = await client.post("/api/bookings", json=payload)
    assert resp1.status_code == 201

    resp2 = await client.post("/api/bookings", json=payload)
    assert resp2.status_code == 409


@pytest.mark.asyncio
async def test_double_booking_different_event_types(client):
    et1 = (await client.post(
        "/api/admin/event-types",
        json={"name": "A", "description": "x", "duration_minutes": 30},
    )).json()
    et2 = (await client.post(
        "/api/admin/event-types",
        json={"name": "B", "description": "x", "duration_minutes": 60},
    )).json()

    future = (datetime.now(timezone.utc) + timedelta(days=1)).replace(
        hour=10, minute=0, second=0, microsecond=0, tzinfo=timezone.utc
    )

    resp1 = await client.post(
        "/api/bookings",
        json={"event_type_id": et1["id"], "start_time": future.isoformat()},
    )
    assert resp1.status_code == 201

    resp2 = await client.post(
        "/api/bookings",
        json={"event_type_id": et2["id"], "start_time": future.isoformat()},
    )
    assert resp2.status_code == 409
