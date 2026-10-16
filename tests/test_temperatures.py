from fastapi.testclient import TestClient
import pytest

from health_service.main import app


client = TestClient(app)
PATH = "/temperatures"
EXPECTED_CAPITALS = [
    {"city": "London", "country": "United Kingdom", "temperatureC": 12},
    {"city": "Paris", "country": "France", "temperatureC": 14},
    {"city": "Berlin", "country": "Germany", "temperatureC": 10},
    {"city": "Rome", "country": "Italy", "temperatureC": 20},
    {"city": "Madrid", "country": "Spain", "temperatureC": 22},
    {"city": "Lisbon", "country": "Portugal", "temperatureC": 18},
    {"city": "Amsterdam", "country": "Netherlands", "temperatureC": 11},
    {"city": "Brussels", "country": "Belgium", "temperatureC": 12},
    {"city": "Vienna", "country": "Austria", "temperatureC": 13},
    {"city": "Prague", "country": "Czechia", "temperatureC": 9},
]


def test_european_capital_temperatures_returns_fixed_mock_readings() -> None:
    response = client.get(PATH)

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {
        "source": "mock",
        "temperatures": EXPECTED_CAPITALS,
    }


def test_european_capital_temperatures_are_repeatable() -> None:
    first = client.get(PATH)
    second = client.get(PATH)

    assert first.status_code == second.status_code == 200
    assert first.json() == second.json()
    assert first.json() == {"source": "mock", "temperatures": EXPECTED_CAPITALS}


@pytest.mark.parametrize("method", ["POST", "PUT", "PATCH", "DELETE"])
def test_european_capital_temperatures_rejects_other_methods(method: str) -> None:
    response = client.request(method, PATH)

    assert response.status_code == 405
    assert response.headers["allow"] == "GET"
