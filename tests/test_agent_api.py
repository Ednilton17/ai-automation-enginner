import pytest

from fastapi.testclient import TestClient

from app.core.dependencies import get_agent_service
from app.main import app


class FakeAgentService:

    async def run(self, message: str) -> str:
        return f"Fake response: {message}"


def override_agent_service() -> FakeAgentService:
    return FakeAgentService()


@pytest.fixture
def client():

    app.dependency_overrides[get_agent_service] = (
        override_agent_service
    )

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()


def test_run_agent_should_return_response(client):

    response = client.post(
        "/api/v1/agent/run",
        json={
            "message": "Create invoice"
        }
    )

    assert response.status_code == 200

    assert response.json() == {
        "response": "Fake response: Create invoice"
    }


def test_run_agent_should_reject_empty_message(client):

    response = client.post(
        "/api/v1/agent/run",
        json={
            "message": ""
        }
    )

    assert response.status_code == 422


def test_run_agent_should_reject_missing_message(client):

    response = client.post(
        "/api/v1/agent/run",
        json={}
    )

    assert response.status_code == 422


def test_run_agent_should_reject_message_over_limit(client):

    response = client.post(
        "/api/v1/agent/run",
        json={
            "message": "a" * 4001
        }
    )

    assert response.status_code == 422