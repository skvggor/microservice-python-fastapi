# python-fastapi

<!-- ## Docker -->

<!-- add docker instructions here -->

## Prepare

```bash
python3 -m venv venv
source venv/bin/activate
pip-compile requirements.in
```

## Installation

```bash
pip install -r requirements.txt
```

## Run

### Development

```bash
fastapi dev main.py
```

### Production

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Test

```bash
pytest
```
