from functools import lru_cache

from config import Settings


@lru_cache
def get_settings() -> Settings:
    return Settings()


def test_config():
    assert get_settings().current_prefix == "v1"
    assert get_settings().port == 8000
    assert get_settings().app_name == "Microservice App"
