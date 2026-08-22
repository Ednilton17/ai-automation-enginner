import pytest
from httpx import AsyncClient


@pytest.mark.anyio
async def test_health_should_return_up(
    client: AsyncClient
):

    response = await client.get("/health")

    assert response.status_code == 200

    body = response.json()

    assert body["status"] == "UP"
    assert body["environment"] == "development"

@pytest.mark.anyio
async def test_health_should_have_expected_fields(
    client: AsyncClient
):

    response = await client.get("/health")

    body = response.json()

    assert "status" in body
    assert "environment" in body

@pytest.mark.anyio
async def test_unknown_endpoint_should_return_404(
    client: AsyncClient
):

    response = await client.get(
        "/endpoint-that-does-not-exist"
    )

    assert response.status_code == 404

    body = response.json()

    assert body["detail"] == "Not Found"