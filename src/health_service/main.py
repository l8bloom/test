"""FastAPI application for the health service."""

from fastapi import FastAPI

app = FastAPI(title="Health service")


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


@app.get("/ping")
def ping() -> dict[str, str]:
    """Answer a liveness probe with a static reply."""
    return {"message": "pong"}
