from fastapi import APIRouter, Depends

from src.v1.privateendpoint.service import get_data

from src.v1.privateendpoint.models import (
    PrivateEndpointPayloadModel,
    PrivateEndpointResponseModel
)

router = APIRouter()

get_doc = {
    200: {
        "content": {
            "application/json": {
                "example": {
                    "fullname": "first_name last_name"
                }
            }
        }
    }
}


@router.get("/privateendpoint",
            tags=["Private endpoint"],
            responses=get_doc,
            response_model=PrivateEndpointResponseModel)
async def privateendpoint(
    model: PrivateEndpointPayloadModel = Depends()
) -> PrivateEndpointResponseModel:
    """
        Return data from service.
    """
    response = get_data(model)

    return response
