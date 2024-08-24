from pydantic import BaseModel


class HealthCheckResponseModel(BaseModel):
    status: str
