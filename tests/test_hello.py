from fastapi.testclient import TestClient

from health_service.main import app


client = TestClient(app)


def test_hello_returns_greeting() -> None:
    response = client.get("/hello")

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {"message": "Hello, world!"}

