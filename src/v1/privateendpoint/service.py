from src.config import Settings

from src.v1.privateendpoint.models import (
    PrivateEndpointPayloadModel,
    PrivateEndpointResponseModel
)

settings = Settings()


def get_data(
    model: PrivateEndpointPayloadModel
) -> PrivateEndpointResponseModel:
    """
        Return data from endpoint.
    """
    params = model.model_dump()

    first_name = params.get("first_name")
    last_name = params.get("last_name")

    return PrivateEndpointResponseModel(
        fullname=f"{first_name} {last_name}"
    )
