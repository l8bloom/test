"""FastAPI application for the health service."""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Health service")

ENDPOINTS_PAGE = """<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Service endpoints</title>
    <style>
        body {
            font-family: Arial, Helvetica, sans-serif;
            margin: 24px;
        }
        h1 {
            font-size: 32px;
            margin: 16px 0 24px;
        }
        table {
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #d0d7d3;
            padding: 10px 16px;
            text-align: left;
        }
        thead th {
            background-color: #2e7d5b;
            color: #ffffff;
        }
        tbody tr:nth-child(even) {
            background-color: #f2f5f3;
        }
    </style>
</head>
<body>
    <h1>Service endpoints</h1>
    <table>
        <thead>
            <tr>
                <th>Path</th>
                <th>Verb</th>
                <th>Owner</th>
                <th>On call</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>/hello</td>
                <td>GET</td>
                <td>Team Kestrel</td>
                <td>Weekdays</td>
            </tr>
            <tr>
                <td>/health</td>
                <td>GET</td>
                <td>Team Osprey</td>
                <td>Always</td>
            </tr>
            <tr>
                <td>/goodbye</td>
                <td>GET</td>
                <td>Team Heron</td>
                <td>Weekends</td>
            </tr>
        </tbody>
    </table>
</body>
</html>
"""


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


@app.get("/endpoints", response_class=HTMLResponse)
def endpoints() -> str:
    """Render the service endpoints table from the mockup."""
    return ENDPOINTS_PAGE
