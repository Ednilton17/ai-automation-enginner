from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_health_should_return_200():
    response = client.get("/health")    
    assert response.status_code == 200

    body = response.json()

    assert body["status"]== "UP"
    assert "environment" in body


