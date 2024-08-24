# microservice-python-fastapi

WORK IN PROGRESS

A scaffold for microservices using Python and FastAPI. This project is intended to be used as a template for new projects.

---

[![microservice-python-fastapi](https://github.com/skvggor/microservice-python-fastapi/actions/workflows/build-and-testing.yml/badge.svg)](https://github.com/skvggor/microservice-python-fastapi/actions/workflows/build-and-testing.yml)

---

## Dependencies (docker)

-   Docker
-   Docker Compose

### Set .env

```bash
cp .env.example .env
```

### Run

```bash
docker-compose up --build
```

## Dependencies (local)

-   Python 3.10+
-   Pip + virtualenv

### Prepare

```bash
python3 -m venv venv
source venv/bin/activate
pip install pip-tools
pip-compile requirements.in
```

### Installation

```bash
pip install -r requirements.txt
```

### Run

#### Development

```bash
fastapi dev main.py
```

#### Production

```bash
fastapi run --host 0.0.0.0 --port 8000
```

### Test

```bash
pytest
```

### Coverage

```bash
pytest -vv --cov=. --cov=src --cov-report=term-missing --cov-report=xml .
```
