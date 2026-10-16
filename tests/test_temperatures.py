from fastapi.testclient import TestClient

from health_service.main import app


client = TestClient(app)
PATH = "/temperatures/european-capitals"
EXPECTED_CAPITALS = [
    {"city": "Amsterdam", "country": "Netherlands", "temperatureC": 12},
    {"city": "Berlin", "country": "Germany", "temperatureC": 11},
    {"city": "Copenhagen", "country": "Denmark", "temperatureC": 9},
    {"city": "London", "country": "United Kingdom", "temperatureC": 13},
    {"city": "Madrid", "country": "Spain", "temperatureC": 21},
    {"city": "Oslo", "country": "Norway", "temperatureC": 6},
    {"city": "Paris", "country": "France", "temperatureC": 14},
    {"city": "Prague", "country": "Czechia", "temperatureC": 10},
    {"city": "Rome", "country": "Italy", "temperatureC": 19},
    {"city": "Vienna", "country": "Austria", "temperatureC": 12},
]


def test_european_capital_temperatures_returns_fixed_mock_readings() -> None:
    response = client.get(PATH)

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {
        "source": "mock",
        "unit": "celsius",
        "capitals": EXPECTED_CAPITALS,
    }


def test_european_capital_temperatures_are_repeatable() -> None:
    first = client.get(PATH)
    second = client.get(PATH)

    assert first.status_code == second.status_code == 200
    assert first.json() == second.json()
    assert "observedAt" not in first.json()


def test_european_capital_temperatures_rejects_post() -> None:
    response = client.post(PATH)

    assert response.status_code == 405
    assert response.headers["allow"] == "GET"
