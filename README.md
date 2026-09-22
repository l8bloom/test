# Health service

A minimal FastAPI service with a process health endpoint.

## Requirements

- Python 3.12 or newer

## Install

Create and activate a virtual environment, then install the service and test
dependencies:

```shell
python -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[test]'
```

## Test

```shell
pytest
```

## Run

```shell
uvicorn health_service.main:app --host 0.0.0.0 --port 8000
```

The health endpoint is available at `http://localhost:8000/health`.
