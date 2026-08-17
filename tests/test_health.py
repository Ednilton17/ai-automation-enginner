from fastapi.testclient import TestClient

from httpx import ASGITransport, AsyncClient
from app.main import app

import pytest

client = TestClient(app)

def test_health_should_return_200():
    response = client.get("/health")    
    assert response.status_code == 200

    body = response.json()

    assert body["status"]== "UP"
    assert "environment" in body

@pytest.mark.anyio
async def test_health_should_return_up():

    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test"
    ) as client:

        response = await client.get("/health")

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "UP"
    assert body["environment"] == "development"

@pytest.mark.anyio
async def test_unknown_route_should_return_404():

    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test"
    ) as client:

        response = await client.get(
            "/route-that-does-not-exist"
        )

    assert response.status_code == 404
