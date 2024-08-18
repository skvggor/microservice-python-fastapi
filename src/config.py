from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    port: int = 8000
    app_name: str = "Awesome Microservice"
    current_preffix: str = "v2"

    model_config = SettingsConfigDict(env_file=".env")
