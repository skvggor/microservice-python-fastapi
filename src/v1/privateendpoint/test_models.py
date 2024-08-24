from models import (
    PaginationModel,
    PrivateEndpointResponseModel,
    PrivateEndpointPayloadModel
)


def test_pagination_model():
    pagination = PaginationModel(
        current_page=1,
        items_per_page=10,
        total_pages=5,
        total_items=50
    )

    assert pagination.total_pages == 5
    assert pagination.total_items == 50


def test_private_endpoint_response_model():
    response = PrivateEndpointResponseModel(
        fullname="Skvggor Betraktar"
    )

    assert response.fullname == "Skvggor Betraktar"


def test_private_endpoint_payload_model():
    payload = PrivateEndpointPayloadModel(
        first_name="Skvggor",
        last_name="Betraktar"
    )

    assert payload.first_name == "Skvggor"
    assert payload.last_name == "Betraktar"
