from fastapi import FastAPI

from src.config import Settings

from src.v1.healthcheck import router as health_check
from src.v1.privateendpoint import router as private_endpoint

settings = Settings()

app = FastAPI(title=settings.app_name)

app.include_router(health_check.router,
                   prefix=f"/api/{settings.current_prefix}")

app.include_router(private_endpoint.router,
                   prefix=f"/api/{settings.current_prefix}")
