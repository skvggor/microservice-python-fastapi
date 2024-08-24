FROM python:3.12-slim

RUN pip install --upgrade pip
RUN pip install pip-tools

RUN adduser --system --no-create-home nonroot

WORKDIR /app

COPY ./requirements.in /app/requirements.in
RUN pip-compile -r requirements.in
RUN pip install -r requirements.txt

USER nonroot

COPY main.py /app/main.py
COPY src /app/src

CMD ["fastapi", "run"]
