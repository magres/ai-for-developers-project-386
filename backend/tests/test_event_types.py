import pytest


@pytest.mark.asyncio
async def test_list_event_types_empty(client):
    resp = await client.get("/api/event-types")
    assert resp.status_code == 200
    assert resp.json() == []


@pytest.mark.asyncio
async def test_create_event_type(client):
    payload = {"name": "30-min Chat", "description": "Quick call", "duration_minutes": 30}
    resp = await client.post("/api/admin/event-types", json=payload)

    assert resp.status_code == 201
    data = resp.json()
    assert data["name"] == "30-min Chat"
    assert data["description"] == "Quick call"
    assert data["duration_minutes"] == 30
    assert "id" in data


@pytest.mark.asyncio
async def test_create_event_type_invalid_duration(client):
    payload = {"name": "Bad", "description": "x", "duration_minutes": -5}
    resp = await client.post("/api/admin/event-types", json=payload)
    assert resp.status_code == 422


@pytest.mark.asyncio
async def test_list_event_types_after_creation(client):
    await client.post(
        "/api/admin/event-types",
        json={"name": "A", "description": "desc", "duration_minutes": 30},
    )
    await client.post(
        "/api/admin/event-types",
        json={"name": "B", "description": "desc", "duration_minutes": 60},
    )

    resp = await client.get("/api/event-types")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) == 2
    assert data[0]["name"] == "A"
    assert data[1]["name"] == "B"
