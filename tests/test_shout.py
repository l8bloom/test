from fastapi.testclient import TestClient

from health_service.main import app


client = TestClient(app)


def test_shout_uppercases_and_exclaims() -> None:
    response = client.get("/shout", params={"text": "langgraph is fun"})

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {"message": "LANGGRAPH IS FUN!!!"}


def test_shout_defaults_to_hello() -> None:
    response = client.get("/shout")

    assert response.status_code == 200
    assert response.json() == {"message": "HELLO!!!"}
