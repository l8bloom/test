"""FastAPI application for the health service."""

from fastapi import FastAPI

app = FastAPI(title="Health service")


@app.get("/dummy")
def dummy() -> dict[str, str]:
    """Return a static response for connector and deployment checks."""
    return {"message": "dummy"}


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
