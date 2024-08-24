from fastapi import APIRouter

from src.v1.healthcheck.models import HealthCheckResponseModel

router = APIRouter()

doc = {
    200: {
        "content": {
            "application/json": {
                "example": {"status": "OK"}
            }
        }
    }
}


@router.get("/healthcheck",
            tags=["Health check"],
            responses=doc)
async def health_check() -> HealthCheckResponseModel:
    """
        Return a status of OK to check if
        the application is working correctly.
    """
    return {"status": "OK"}
