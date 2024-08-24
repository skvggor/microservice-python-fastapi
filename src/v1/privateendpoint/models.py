from pydantic import BaseModel


class PaginationModel(BaseModel):
    current_page: int
    items_per_page: int
    total_pages: int
    total_items: int


class PrivateEndpointPayloadModel(BaseModel):
    first_name: str
    last_name: str


class PrivateEndpointResponseModel(BaseModel):
    fullname: str
