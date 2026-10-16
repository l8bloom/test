"""FastAPI application for the health service."""

from fastapi import FastAPI

app = FastAPI(title="Health service")

CAPITAL_TEMPERATURES = [
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


@app.get("/temperatures/european-capitals")
def european_capital_temperatures() -> dict[str, object]:
    """Return fixed mock Celsius temperatures for ten European capitals."""
    return {"source": "mock", "unit": "celsius", "capitals": CAPITAL_TEMPERATURES}


@app.get("/hello")
def hello() -> dict[str, str]:
    """Return a static greeting."""
    return {"message": "Hello, world!"}


@app.get("/health")
def health() -> dict[str, str]:
    """Report that the service process is healthy."""
    return {"status": "ok"}


@app.get("/goodbye")
def goodbye() -> dict[str, str]:
    """Return a static farewell."""
    return {"message": "Goodbye, world!"}
