from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/api/v1/healthcheck")

    assert response.status_code == 200
    assert response.json() == {"status": "OK"}
