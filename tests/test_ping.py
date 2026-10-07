from fastapi.testclient import TestClient

from health_service.main import app


client = TestClient(app)


def test_ping_returns_pong() -> None:
    response = client.get("/ping")

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {"message": "pong"}
