from fastapi.testclient import TestClient

from health_service.main import app


client = TestClient(app)


def test_health_returns_ok() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {"status": "ok"}


def test_health_rejects_post() -> None:
    response = client.post("/health")

    assert response.status_code == 405
