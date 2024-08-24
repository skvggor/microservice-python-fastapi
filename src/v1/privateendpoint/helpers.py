from math import ceil

from src.config import Settings

settings = Settings()


def mount_pagination(
    items: list,
    current_page: int,
    items_per_page: int,
) -> dict:
    """
        Mount the pagination object.
    """
    start = (current_page - 1) * items_per_page
    end = start + items_per_page
    paginated_items = items[start:end]

    return {
        "items": paginated_items,
        "pagination": {
            "current_page": current_page,
            "items_per_page": items_per_page,
            "total_pages": ceil(len(items) / items_per_page),
            "total_items": len(items),
        }
    }
