"""FastAPI application for the health service."""

from typing import TypedDict

from fastapi import FastAPI
from langgraph.graph import END, START, StateGraph

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


class ShoutState(TypedDict):
    text: str


def _uppercase(state: ShoutState) -> ShoutState:
    return {"text": state["text"].upper()}


def _exclaim(state: ShoutState) -> ShoutState:
    return {"text": state["text"] + "!!!"}


_shout_builder = StateGraph(ShoutState)
_shout_builder.add_node("uppercase", _uppercase)
_shout_builder.add_node("exclaim", _exclaim)
_shout_builder.add_edge(START, "uppercase")
_shout_builder.add_edge("uppercase", "exclaim")
_shout_builder.add_edge("exclaim", END)
shout_graph = _shout_builder.compile()


@app.get("/shout")
def shout(text: str = "hello") -> dict[str, str]:
    """Run the text through a LangGraph graph that uppercases it and adds exclamation marks."""
    result = shout_graph.invoke({"text": text})
    return {"message": result["text"]}
