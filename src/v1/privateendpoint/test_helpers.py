from math import ceil

from helpers import mount_pagination

from src.config import Settings

settings = Settings()


def test_mount_pagination_basic():
    items = list(range(1, 21))
    current_page = 2
    items_per_page = 5

    result = mount_pagination(items, current_page, items_per_page)

    assert result["items"] == [6, 7, 8, 9, 10]
    assert result["pagination"]["current_page"] == current_page
    assert result["pagination"]["items_per_page"] == items_per_page
    assert result["pagination"]["total_pages"] == ceil(
        len(items) / items_per_page)
    assert result["pagination"]["total_items"] == len(items)


def test_mount_pagination_last_page():
    items = list(range(1, 21))
    current_page = 4
    items_per_page = 6

    result = mount_pagination(items, current_page, items_per_page)

    assert result["items"] == [19, 20]
    assert result["pagination"]["current_page"] == current_page
    assert result["pagination"]["total_pages"] == ceil(
        len(items) / items_per_page)


def test_mount_pagination_empty_items():
    items = []
    current_page = 1
    items_per_page = 5

    result = mount_pagination(items, current_page, items_per_page)

    assert result["items"] == []
    assert result["pagination"]["total_items"] == 0
    assert result["pagination"]["total_pages"] == 0
