from fastapi.testclient import TestClient

from health_service.main import app


client = TestClient(app)


def test_goodbye_returns_farewell() -> None:
    response = client.get("/goodbye")

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {"message": "Goodbye, world!!"}
