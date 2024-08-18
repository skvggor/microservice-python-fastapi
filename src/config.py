from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    port: int
    app_name: str
    current_prefix: str

    model_config = SettingsConfigDict(env_file=".env")
