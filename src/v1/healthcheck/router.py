from fastapi import APIRouter
from src.config import Settings

settings = Settings()

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
            tags=[f"/api/{settings.current_prefix}/healthcheck"],
            responses=doc)
async def health_check():
    """
    Retorna um status de OK para verificar
    se a aplicação está funcionando corretamente.
    """

    return {"status": "OK"}
