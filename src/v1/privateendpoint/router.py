from fastapi import APIRouter
from src.config import Settings

settings = Settings()

router = APIRouter()

doc = {
    200: {
        "content": {
            "application/json": {
                "example": {"from_user_param": "from_user_param"}
            }
        }
    }
}


@router.get("/private-endpoint/{from_user_param}",
            tags=[f"/api/{settings.current_prefix}/private-endpoint"],
            responses=doc)
async def private_endpoint(from_user_param: str):
    """
    Retorna um parâmetro recebido.
    """

    return {"from_user_param": from_user_param}
