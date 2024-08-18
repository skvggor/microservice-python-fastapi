from functools import lru_cache

from fastapi import FastAPI

from src.config import Settings

from src.v1.healthcheck import router as health_check

app = FastAPI()


@lru_cache
def get_settings() -> Settings:
    return Settings()


app.include_router(health_check.router,
                   prefix="/api/" + get_settings().current_prefix)
