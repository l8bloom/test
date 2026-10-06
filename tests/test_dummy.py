"""API contract tests for the dummy endpoint introduced by CR-17.

https://platform.dev.rokolabs.ai/clients/domagoj/projects/localproject/change-requests/17
"""

from fastapi.testclient import TestClient

from health_service.main import app


client = TestClient(app)


def test_dummy_returns_fixed_json_response() -> None:
    # Request the dummy endpoint.
    response = client.get("/dummy")

    # Verify the complete success contract.
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {"message": "dummy"}


def test_dummy_rejects_post() -> None:
    # Request the dummy endpoint with an unsupported method.
    response = client.post("/dummy")

    # Verify the method refusal contract.
    assert response.status_code == 405
    assert response.headers["content-type"] == "application/json"
    assert response.headers["allow"] == "GET"
    assert response.json() == {"detail": "Method Not Allowed"}


def test_dummy_returns_the_same_response_repeatedly() -> None:
    # Request the stateless endpoint twice.
    first_response = client.get("/dummy")
    second_response = client.get("/dummy")

    # Verify repeat calls return the same observable result.
    assert first_response.status_code == 200
    assert second_response.status_code == 200
    assert first_response.headers["content-type"] == "application/json"
    assert second_response.headers["content-type"] == "application/json"
    assert first_response.json() == {"message": "dummy"}
    assert second_response.json() == first_response.json()
