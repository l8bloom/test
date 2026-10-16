"""FastAPI application for the health service."""

from fastapi import FastAPI

app = FastAPI(title="Health service")

CAPITAL_TEMPERATURES = [
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


@app.get("/temperatures")
def european_capital_temperatures() -> dict[str, object]:
    """Return fixed mock Celsius temperatures for ten European capitals."""
    return {"source": "mock", "temperatures": CAPITAL_TEMPERATURES}


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
